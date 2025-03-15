## Accessing Text Data FAQ

 For Assignment 3 and your project, you'll need to access LLM data. The instructions for both are relatively open-ended. Here are some snippets and tips that might be useful.


### Approach 1: just download files from urls

If you visit the files section of the Dolma dataset (here: https://huggingface.co/datasets/allenai/dolma/tree/main/urls), you'll see a `urls` directory, with a bunch of text files. Each text files has a list of urls, and (we can assume) those urls contain data.

(ex: in https://huggingface.co/datasets/allenai/dolma/blob/main/urls/v1_6-sample.txt, we find a link to https://olmo-data.org/dolma-v1_6-8B-sample/v1_5r2_sample-0000.json.gz)

So one option might be to randomly sample a set of these URLs (perhaps downloading v1_6-sample.txt loading into a Python list or Pandas DF or other structure of your choice, and using something like random.choice(), df.sample(), etc.), then using your favorite approach to make http requests (`requests` lib, curl from your CLI, your web browser, etc.) to download those files. You'll need to inspect the contents (unzip, then perhaps use `head` or a Pythons script to take a look at the first few lines) and then can finally load into your preferred data science environment (repl, notebook, etc) to proceed.


### Approach 2: download files directly from HF

If you visit the files section for RefinedWeb (here: https://huggingface.co/datasets/tiiuae/falcon-refinedweb/tree/main), you'll find directories with the data files directly included. You can go ahead and just start downloading from web browser if you want! Again, a similar approach here might be to select a sample of file names and grab them all.


### Approach 3: Dataset library

The HuggingFace datasets library supports loading data via a single function call.


```
dataset = load_dataset("your_large_dataset", streaming=True)
```

If the dataset is large, getting a true random sample will be hard. But you can explore "reservoir sampling" (https://en.wikipedia.org/wiki/Reservoir_sampling) or just use a buffer and shuffle that and it's reasonable for this assignment.

This option is likely fastest if you've already used/installed `datasets`, and might be a good idea to play around with if you plan to use this for your project.

## Other FAQS

Do I need to convert words to tokens, or how should I count the tokens?

- First of all, you may simply state the assumption that you assume 1 word = 1 token. You may also make a rough estimate based on common ratios (see e.g. https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them and play around yourself here https://platform.openai.com/tokenizer).


Can I be sure I'm getting a true random sample for some target distribution?

- In short, not really (for assignment purposes, any reasonable attempt with accompanying assumptions is ok). We'll discuss when we "debrief" on the assignment.

I'm not sure my chosen text dataset is acceptable!

- If it's a large text dataset with at least 300,000 words or tokens, you're good to go.