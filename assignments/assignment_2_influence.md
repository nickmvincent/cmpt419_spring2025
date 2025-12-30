# Assignment 2

DEADLINE (Spring 2025): Mar 4, 23:59

Our Module 2 content is focused on understanding the broad question: *Which groups of observations – or groups of people – are “responsible” for a given model output or “capability”?*

In this assignment, we'll get some hands-on experience with the concept of training data influence.

There are four parts to the assignment. You'll need to write code to train a ML model and produce influence values for some of the training data in the model. Below, the requirements for each part are described.

Each part will have a coding component and a report component. You will turn in one file (or multiple) with code (e.g., a `.py` file or `.ipynb` file) and one report PDF. If using computational notebooks like a Jupyter notebook, you may combine these two into a single file (e.g. a notebook exported to a PDF with code visible.

In your code, you can use comments to designate which parts of your code correspond to each part.

Note 1: you may work on this assignment in groups of 1-3.

Note 2: you may use generative AI on this assignment, and must report your use. FYI – the instructor has tried out several models, and they’re definitely useful, but you’ll need to be careful about explaining your choices. In fact, I’ll even provide you some example outputs of what you get from directly copy-pasting the assignment into several strong models!

Note 3: Finally, as an additional incentive to avoid literally just copy-pasting the assignment into your favorite consumer AI product, I may randomly select some students to explain their solutions in class.

### **Part 1: Preliminaries**

First, you should select a dataset to work with, define a specific classification (must do classification for this assignment) task, and establish a baseline model.

If you're looking for inspiration, you might consider selecting something from [https://archive.ics.uci.edu/](https://archive.ics.uci.edu/)

You will not be graded based on your dataset choice, task choice, or achieving a certain level of performance.

Rather, you will be graded based on your ability to describe, in a scientifically complete fashion, the choices you've made.

You are recommended to select a dataset from a domain of your interest and then take a small random sample of that dataset (e.g., 10000 rows -- though you can lower this if using high-dimensional data, want to use deep learning, etc. -- ask us if you're unsure) to ensure that you can complete this assignment quickly, without being burdened by excessive computational costs. What constitutes "excessive" here will depend on your access to computing resources (you may wish to explore using an online tool with some degree of free compute like Google Colab).

If you select a dataset you are interested in, you may be able to reuse some of your code you write for this assignment for your project.

Suggested approach: I recommend first training several models on the "full dataset" (e.g. logistic regression, basic random forest, KNN, XGBoost). See how long this takes. Then, try subsampling 10% or 1% of your data and see if the training time falls low enough that you think you can reasonably retrain a model at least 50 total times. (if a training run takes a day and you have a week left... this is too much training time!)

Specifically, you should write code to do the following:

* Load a dataset into memory. Describe the dataset in your report. (2 marks)  
* Process into features and labels. Describe the features and labels in your report. (2 marks)  
* Split into train and test sets. Describe your specific approach (e.g. random 80/20 split, time-based split, etc.) (2 marks)  
* Train some classifier. It does not need to be the "best" possible performance for your chosen dataset, though you may want to try a few options if feasible to do so. (2 marks) 
  * You should list some reason for your choice of classifier. 
* Report performance of your baseline classifier: accuracy, confusion matrix. You are encouraged to include a precision-recall curve or TPR vs. FPR curve (i.e. AUROC curve), though if you think it isn't helpful you can just mention why not. You must choose a "primary metric" that you will use for your data value estimates, and you should justify this choice. (2 marks)
  * Why is this measurement appropriate for the data/task you chose?

10 marks total for part 1

### **Part 2: Brute force LOO influence**

Next, you should select (manually or randomly) 10 training data points (i.e., observations) and compute the exact leave-one-out LOO influence of these examples on your chosen primary metric.

You can earn up to 4 marks for clean and correct code.

Report the influence score for each of your observations. You may do this in a table or plot. (2 marks).

Please briefly comment on any trends you observe with your influence scores. Are any points with high influence unusual in any way? It's OK if they're not, but you should demonstrate that you looked. (2 marks)

8 marks total for part 2\.

### **Part 3: Group-level influence**

Next, you should select (manually or randomly) 10 different *groups* of data points of different sizes. For instance, you might randomly select 10%, 20%, 30%, etc. of the training data. You should compute the exact leave-entire-group-out influence for each group.

You can earn up to 4 marks for clean and correct code.

Report the influence score for each of your groups. (2 marks)

For part 3, you must also include a plot that shows group size compared with influence. (2 marks)

8 marks total for part 3\.

### **Part 4: Shapley values**

Finally, we will roughly estimate Shapley values for our training data.

For each observation and each group, you should compute the Shapley value using Truncated Monte Carlo Shapley Value Estimation (described briefly in our survey reading and in more detail here: [http://proceedings.mlr.press/v97/ghorbani19c/ghorbani19c.pdf](http://proceedings.mlr.press/v97/ghorbani19c/ghorbani19c.pdf)).

This will involve a coding challenge: implementing this particular Shapley value estimation algorithm.

In the Ghorbani and Zou paper, the authors suggest using a truncation cut-off: if performance for a given point / time step is very close to full performance V(D), we don't need to retrain again.

We will go a step further and use the following rule to ensure our code doesn't take too long to run: we should take our best guess at the Shapley value for each training data point after only 10 total permutations have been examined. In other words, your code should just re-shuffle the training data 10 times, compute the marginal impact of each training point, and then average these across the 10 permutations.

Furthermore, you may further subsample your training data (E.g. if you started with 100k rows and have only been using 10k so far, and need to drop down to 1k... you can) for this part if needed to complete the assignment in time.

You can earn up to 4 marks for clean and correct code.

Here, you need only to plot the distribution of all Shapley values. (2 marks)

If you have extra time, you are encouraged to compute more accurate Shapley value estimates by using more permutations and compare the Shapley values to LOO influence from part 2, but this is optional.

6 marks total for part 4.

### **Grading**

This assignment will be graded based on both code correctness and an accompanying report. You can earn marks for each of these separately (i.e. if you have errors in your influence calculations, you can still earn the marks for reporting and visualizing the potentially erroneous data values).

To recap, there are:

* 10 marks available in part 1  
* 8 in part 2  
* 8 in part 3  
* 6 in part 4  
* for a total of 32 marks.

Part 4 will likely be the most difficult, but offers the least marks, so you should consider completing the earlier sections first.

If you submitted with a group, your report must include a 'contribution statement' that describes how each member contributed.