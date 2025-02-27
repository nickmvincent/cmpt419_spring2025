# Assignment 3

DEADLINE (Spring 2025): Mar 20, 23:59

Our Module 3 content will focus on understanding datasets from online platforms and elsewhere. This will be helpful in both understanding LLM pre-training data, and should also be helpful in making progress on your project.

In this assignment, we'll inspect two datasets: a large text dataset and a second dataset from any domain that chose (either because of personal interest or because it helps you make progress on your project).

Some learning goals:
- Understand the process by which you might gather a very large web-scale dataset (we will not actually download any full datasets, however!)
- Get experience with dataset documentation practices
- Get experience with the "just look at your data!" hack

You may want to  use:
- https://huggingface.co/docs/datasets/en/index
- https://github.com/allenai/wimbd


## Part 1: Getting some data (4 marks)

First, you should gain access to a small sample of LLM training data. You may use Dolma (https://allenai.github.io/dolma/), RefinedWeb (https://huggingface.co/datasets/tiiuae/falcon-refinedweb), or any other source you've come across.

The main challenge of part 1 is acquiring a good sample.

Your goal is to acquire 300k tokens (about 0.01% of the 3 trillion token in Dolma).

For part 1, write a short 'methods' section and key code you used to get a random sample of LLM pre-training data onto your machine (3 marks).

Second, write a short 'methods' section that describes the dataset you chose based on your project/interests (1 mark).


## Part 2: Datasheets (8 marks)

Next, you should visit https://arxiv.org/pdf/1803.09010 and answer all the questions in Section 3.2 for both datasets. (4 marks)


## Part 3: Data Assessment (8 marks)

Next, you should prepare a random sample of 10 "observations" from each dataset. We will be manually assessing their quality!
You should produce a table that shows each observation and some kind of "assessment column" of your choosing. For instance, you might manually assess the "usefulness" to a certain task. You might consider the toxicity of the content (in the text domain).

To create this "assessment column", you will likely need to make some subjective choices. You could create a quantitative assessment as well (e.g., the number of times of a key word appears in text data).

Please describe and briefly justify your chosen metric. For your project dataset, you're encouraged to select something relevant to your project. The point of this assignment is to provide a forcing function to "look at your data", which is a common adage and suggestion for all kinds of AI projects! (4 marks) 

Section 3a of your report will consist of two tables, with 10 rows and at least 2 columns.

Example row:

"this is a sentence in my LLM training data from a blog", Toxicity score: 0
"this is a really angry mean sentence in my LLM training data", Toxicity score: 10

In your report, you should write a paragraph summarize what you found. Perhaps you were surprised by the text, or perhaps everything was just as expected. (4 marks).

## Submission Instructions

You will turn in:
a single notebook-style report as a PDF file that fulfills all above criteria. You may use a Jupyter notebook, or a Word/Google doc with key code pasted in.