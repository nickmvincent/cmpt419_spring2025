---
theme: default
background: none
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Intro
mdc: true
author: Prof. Nick Vincent
institute: Simon Fraser University
date: 2024-01-15
---

# About

This deck contains lecture content for Jan 15, 2024 and Jan 24, 2024.

---

<!-- Using v-click for animations instead of auto-animate -->
<div class="flex justify-center gap-4">
  <div v-click class="w-50 h-38 bg-[#00ff9f]"></div>
  <div v-click class="w-50 h-38 bg-[#00b8ff]"></div>
  <div v-click class="w-50 h-38 bg-[#001eff]"></div>
  <div v-click class="w-50 h-38 bg-[#bd00ff]"></div>
</div>

---

<div class="relative w-full h-full flex items-center justify-center">
  <div class="absolute w-88 h-88 rounded-full bg-[#00ff9f]"></div>
  <div class="absolute w-64 h-64 rounded-full bg-[#00b8ff]"></div>
  <div class="absolute w-40 h-40 rounded-full bg-[#001eff]"></div>
  <div class="absolute w-16 h-16 rounded-full bg-[#bd00ff]"></div>
</div>

---

# Block 1

For the Spring 2024 term, this was presented on 2024-01-15.

---

# While we file in

<v-clicks>

- Check out Piazza link (Canvas announcements)
- Anyone have AI-related news they want to discuss
- Feel free to collect your thoughts re: strong reactions to readings

</v-clicks>

---

# Course Logistics

<v-clicks>

- Tentative course calendar on Canvas updated
- Slides will go on GitHub
- Submit reading response by Wed. this week (or email me if you just joined)
- New readings posted

</v-clicks>

---

# Agenda

<v-clicks>

- Today: Discuss readings for this week
- Goals: highlight key takeaways, find areas of interest
- At the end: Intro to readings for next week

</v-clicks>

---

# HCML Reading (Chancellor 2023)

---

# Good and bad uses of AI -- some go to examples

<v-clicks>

- Auto complete
- Predict malignant tumor
- Deep fake
- Discrimination (on many axes)

</v-clicks>

---

# Progress? in AI

<div class="grid grid-cols-2 gap-4">
<div class="col-span-1">

<v-clicks>

- Deep learning "gains" don't always hold up to scrutinty

</v-clicks>

</div>
<div class="col-span-1">

![](figs/worrying_trends.png)

</div>
</div>

<br>

> There are more examples we can discuss! And of course we can keep an eye out for new research news.

---

# People as "objects of prediction"

<v-clicks>

- How to counter this?
  - Fairness, equality, justice
- Note: computing often forces us to precisely define these concepts in a way that's illuminating
- We might disagree

</v-clicks>

---

# Sub-fields of CS

Article mentions we should "refine HCML into a unifying and interdisciplinary force across CS rather than risk fracture with each sub-field of CS taking ownership of an independent vision of HCML"

What's the backstory here?

---

# A bit of behind the scenes into CS research

<v-clicks>

- Subcommunities often run their own conferences
- Drives a lot of the incentives of researchers
- This might matter for research-related jobs in industry too
- e.g., some ML jobs list NeurIps papers as a requirement, some Responsible AI jobs list FAccT

</v-clicks>

---

# Examples

<v-clicks>

- ML people send papers to NeurIPS, ICML, ICLR, and many more
- HCI people send papers to CHI, CSCW, and many more
- Philosophy people send papers to their own, pretty much entirely separate journals

</v-clicks>

---

# Early HCML

<v-clicks>

- Chancellor highlights some of the history -- the "HCI" community and "FAccT" community played major roles
  - FAccT is a relatively new conference which has gained a lot of momentum
- Information Science and STS
- CSCW also plays a major role
- Various social sciences and fields of critical scholarships as well..
- That's a lot of disciplines already

</v-clicks>

---

# Acronym Cheatsheet thus far

<v-clicks>

- HCI: human-computer interaction. Main conference is "CHI", confusingly.
- FAccT: Fairness, Accountability, and Transparency
- CSCW: computer supported cooperative work (and social computing)
- [STS](https://en.wikipedia.org/wiki/Science_and_technology_studies): Science and technology studies. Also, science, technology, and society

</v-clicks>

---

# What Counts as HCML?

---

# Proposed definition statement

"Human-centered machine learning is a set of practices for building, evaluating, deploying, and critiquing ML systems that balances technical innovation with an equivalent focus on human and social concerns."[^1]

[^1]: [Chancellor 2023](https://cacm.acm.org/magazines/2023/3/270209-toward-practices-for-human-centered-machine-learning/fulltext)

---

# We can evaluate different practices to see if they fit in this set

<v-clicks>

- It's possible two different organizations both trying to build an AI system for the same *task* could differ substantially in whether they meet the "human-centered" definition
- People can always disagree about what human and social concerns should be ranked most highly
- But this gives us a starting point

</v-clicks>

---

# Focusing on Practices 

Five categories of suggestions are given, i.e. what can you do when you're a software engineer, manager, research scientist, professor, etc.

<v-clicks>

- should I use ML?
- what's my "position"?[^2]
- users vs. humans
- credit other domains
- iterate on failure

</v-clicks>

[^2]: See e.g. [positionality statements](https://en.wikipedia.org/wiki/Positionality_statement)

---

# What challenges might we expect to face?

---

# Institutional actions

<v-clicks>

- new norms at conference, e.g. negative impact statements (NeurIPS)
- institutional support for interdisciplinary research
- computing (broad) vs. computer science
- support students who want to do interdisciplinary research!

</v-clicks>

---

# Over to DCAI

---

# Problems with data

<v-clicks>

- "Differences in labeling": do you and I agree if a pill is "scratched"? Does my hospital notes system have a different coding system than yours?
- "Emphasis on big data": what about a rare medical condition?
- "Ad hoc data curation": need to systemize?

</v-clicks>

---

# Finding label disputes

<v-clicks>

- We might use tools to find subsets of a dataset with high label dispute
- Influence estimation provides one approach we'll see

</v-clicks>

---

# Domain Expertise

<v-clicks>

- get the biologists to label the cells!
- get former players to provide "labels" for sports analytics
- many more examples
- this is where the DCAI argument really starts to merge with the HCAI argument

</v-clicks>

---

# More info

- https://www.youtube.com/watch?v=TU6u_T-s68Y

---

# What is DataPerf

<v-clicks>

- a so-called "benchmark suite"
- focused on data tasks
- meant to be community run and led 

</v-clicks>

---

# What's a "ML benchmark?"

Conventional model-centric ML definition: "a standard, fixed dataset for model accuracy comparisons and performance measurement" (p2, Mazumber et al)

---

# Some terms

<v-clicks>

- from "Probabilistic Machine Learning: An Introduction", Murphy 2022 (https://probml.github.io/pml-book/book1.html)
- task $T$ to learn mapping $f$ from inputs $x \in X$ to outputs $y \in Y$
- x called features (or covariates, or predictors)
- y is label (or target, or response)
- we have N input-output pairs $D = {(x_n, y_n)}$ for $n \in (1,N)$. D is the training set, N is the sample size.

</v-clicks>

---

# Comparing model-centric benchmark and data-centric benchmark

<v-clicks>

- in model-centric, we have a fixed dataset $D$ and we try a bunch of different ways to find $f$
- change model architecture, change training hyperparameters, change task metrics
- in data-centric, we keep all these fixed and just change $D$

</v-clicks>

---

# Testable concept: is a benchmark data centric

<v-clicks>

- you might imagine a test question that describes several differents tasks and asks you to identify which one is "data-centric"

</v-clicks>

---

# Six data centric operations

data...

<v-clicks>

- parsing
- augmentation
- selection
- quality assessment
- acquisition
- cleaning

</v-clicks>

---

Hold time for:

<v-clicks>

- discuss next week's readings
- questions that have popped up thus far

</v-clicks>