There are no hard prerequisites for this course. The course outline says this:

Students may benefit from having taken a course in AI, ML, or data science (or have equivalent experience from e.g. an internship, a research project, a personal project).

Example SFU courses:
- CMPT 310 - Intro Artificial Intelligence
- CMPT 353 - Computational Data Science
- CMPT 414 - Computer Vision

Having taken an HCI course or relevant social science course (e.g., sociology, economics) is a plus, but students without this experience who want to explore interdisciplinary CS work that is “human-centered” are welcome.

That being said, here are some materials that you can use to assess your readiness for the course. My suggestion is to take a look at the code first and see if it seems completely unfamiliar. If you've taken CMPT 353, this will be very familiar. If this content is unfamiliar, you may want to glance through the sklearn tutorial (https://scikit-learn.org/1.4/tutorial/basic/tutorial.html), or for much for detail, the CMPT 353 lecture notes (https://ggbaker.ca/data-science/).

On the ML theory side of things, you may want to watch the 3Blue1Brown Deep Learning series and see if it seems completely unfamiliar or at least partially familiar: https://www.youtube.com/watch?v=aircAruvnKk

If at least one of these feels decently familiar and the other feels somewhat familiar, you're probably in good shape. We won't have any quiz questions in the course that are directly testing computational data science or deep learning material, but the concepts come up and you'll want to have some basis in one of these areas to develop a good project idea.

In terms of HCI or social science materials, we'll cover background in the course. Any and all perspectives are welcome!


You may also want to check out this ChatGPT-generated exercises below to see some examples of common operations machine learning operations.

```python
# CRASH COURSE: Basic Model Training, Testing, and Data Analysis

# ===========================
# 1. IMPORT LIBRARIES
# ===========================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris

# To display plots inline
%matplotlib inline

# ===========================
# 2. LOAD AND EXPLORE DATA
# ===========================
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

print("First five rows of data:")
display(X.head())

print("Data shape:", X.shape)
print("Target shape:", y.shape)

print("\nClass distribution:")
print(y.value_counts())

# ===========================
# 3. BASIC DATA ANALYSIS
# ===========================
# Statistical summary
print("\nStatistical summary of features:")
display(X.describe())

# Pairplot for a quick visual
sns.pairplot(pd.concat([X, y], axis=1), hue='target', diag_kind='kde')
plt.show()

# ===========================
# 4. TRAIN-TEST SPLIT
# ===========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("\nTraining set size:", X_train.shape)
print("Test set size:", X_test.shape)

# ===========================
# 5. MODEL TRAINING
# ===========================
model = LogisticRegression(max_iter=200)  # Increase max_iter to ensure convergence
model.fit(X_train, y_train)

# ===========================
# 6. MODEL TESTING & EVALUATION
# ===========================
y_pred = model.predict(X_test)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# ===========================
# 7. EXERCISES FOR STUDENTS
# ===========================
print("""
Exercises:
1. Try a different classifier (e.g., RandomForestClassifier) and compare results.
2. Experiment with different test sizes (e.g., test_size=0.3).
3. Visualize the coefficient importances or feature importances for your chosen model.
4. Use other performance metrics (e.g., accuracy_score, precision_score) for evaluation.
5. Analyze how class imbalance might affect results (if you artificially modify 'y').
""")
```

```python
# DEEP LEARNING CRASH COURSE

# ===========================
# 1. IMPORTS & SETUP
# ===========================
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

%matplotlib inline

# ===========================
# 2. LOAD & PREPARE MNIST
# ===========================
# The MNIST dataset has 60,000 training images, 10,000 test images
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to [0, 1]
x_train = x_train.astype("float32") / 255.
x_test  = x_test.astype("float32") / 255.

# Flatten 28x28 images to 784-dimensional vectors for the MLP
x_train_flat = x_train.reshape((x_train.shape[0], 28 * 28))
x_test_flat  = x_test.reshape((x_test.shape[0], 28 * 28))

# ===========================
# 3. BASIC DENSE MODEL
# ===========================
mlp_model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

mlp_model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# ===========================
# 4. TRAIN & EVALUATE (MLP)
# ===========================
history_mlp = mlp_model.fit(
    x_train_flat, y_train,
    validation_split=0.1,
    epochs=5,
    batch_size=64,
    verbose=1
)

test_loss, test_acc = mlp_model.evaluate(x_test_flat, y_test)
print(f"\nMLP Test accuracy: {test_acc:.4f}")

# Optional: Plot training curves
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history_mlp.history['loss'], label='Train Loss')
plt.plot(history_mlp.history['val_loss'], label='Val Loss')
plt.legend()
plt.title("MLP Loss")

plt.subplot(1,2,2)
plt.plot(history_mlp.history['accuracy'], label='Train Acc')
plt.plot(history_mlp.history['val_accuracy'], label='Val Acc')
plt.legend()
plt.title("MLP Accuracy")
plt.show()

# ===========================
# 5. ADVANCED SECTION: BASIC CNN
# ===========================
# Reshape data back to (28, 28, 1)
x_train_cnn = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test_cnn  = x_test.reshape((x_test.shape[0], 28, 28, 1))

cnn_model = keras.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu',
                  input_shape=(28, 28, 1)),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),  # regularize
    layers.Dense(10, activation='softmax')
])

cnn_model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

history_cnn = cnn_model.fit(
    x_train_cnn, y_train,
    validation_split=0.1,
    epochs=5,
    batch_size=64,
    verbose=1
)

test_loss_cnn, test_acc_cnn = cnn_model.evaluate(x_test_cnn, y_test)
print(f"\nCNN Test accuracy: {test_acc_cnn:.4f}")

# ===========================
# 6. EXERCISES FOR STUDENTS
# ===========================
print("""
Exercises:
1. Increase the number of epochs or change batch_size and observe results.
2. Modify the architecture (add more layers/neurons) and see if it improves accuracy.
3. Try different optimizers (RMSprop, SGD) and compare training dynamics.
4. Add Batch Normalization layers to see if training stabilizes.
5. Explore other datasets (CIFAR-10, Fashion-MNIST) for a broader challenge.
""")
```