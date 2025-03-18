---
theme: eloc
background: none
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Week 12
mdc: true
author: Prof. Nick Vincent
institute: Simon Fraser University
date: 
---

# Data Governance

Note: rather than screenshot most of the paper, we'll pull up our readings directly for much of this lecture. This may make for a worse "reading the PDF version" experience, my apologies!

[link](https://dl.acm.org/doi/abs/10.1145/3531146.3534637)

## Goals

Today's lecture: gain exposure to a few different frameworks for data governance.

Some guiding questions (to keep back of mind)

- How are data governance decisions being made now?
- What kind of interaction with "governance" will you have in the future? As a voter, as a modeler, as a data creator, etc.


## Recap: What is governance

From: [WP](https://en.wikipedia.org/wiki/Governance) 

> "Governance is the process of making and enforcing decisions within an organization or society. It encompasses decision-making, rule-setting, and enforcement mechanisms to guide the functioning of an organization or society." 

From the Commission on Global Governance:

> "the sum of the many ways individuals and institutions, public and private, manage their common affairs"" 

Pick your favorite LLM and get an answer like this

---

## C.f. Global Climate Governance

Can be useful to think about data governance as a paralell to climate governance. 

What are the current processes in place to determine how new climate laws are passed, how they're enforced, how they do (or do not) cascade between states

---


Latin for "confer or conferatur", meaning "compare" in English. Abbreviation used for "compare with" [WP](https://en.wikipedia.org/wiki/Cf.)

---

## What's NOT governance...

- Things that happen in nature, outside the scope of an organization... maybe
- You can make a really strong argument for much of the physical and social world being part of, or subject to, some governance process though


Exact categorization of governance or not is not a big deal for our immediate concerns, but the point here is to emphasize the flexibility of the word (and the value of frameworks)

---

## Outline

- The LLM model from Jernite et al. (with a big et al.!)
- CARE principles and indigenous data governance
- (if time) intro to some other perspectives

---

# Data Governance for LLMs

---


## How has Data Governance been affected by the LLM era

Key differences of the LLM era are even more 

- "generality"
- scale

Jernite et al., Section 1: 
> "Wikipedia-scale corpora to close to three orders of magnitude more"

---

## What does it mean to design a new governance structure?

Note: "design a new governance structure" = change the rules or norms (implicitly, it's about policy change and changing implicit rules)

It's ambitious!

---

## The "DSO"

Key idea of this paper is a "Data Stewardship Organization" -- a new org that would act as a facilitator (e.g., talk to data creators and data subjects, but also talk to modelers and legal teams and such)

Another key idea: laws vs tools

---

## Important concerns from the paper to flag

- ML community values performance (Birhane et al., citation 18)
- role of European regulatory drive
- how to share benefits equitably?
- issues with human rights framing (many conflicting documents)
- Critical perspectives: human rights and decoloniality

---

## Specifity of data governance

This paper really focuses on language data, with a call out for human-centric data.

How might other modalities disrupt this proposal?

---

## Another Lifecycle of Data

1. Creation
2. Selection
3. Documentation
4. Dissemination
5. Hosting

--- 

6. Serving
7. Conservation
8. Tracking
9. Versioning
10. Deletion

---

## Actors involved

---


## Different kinds of work (different kinds of rules)

- Work done with data vs. work done around data access/control
- My interpretation: stuff you do once you've loaded `data.csv` or `data.parquet` vs. stuff you do that will get you a different `data.csv`

---

## Contestation

- Important to note that incorporating contestation into data governance framework has the potential to really impact your day to day
- Decent chance you might have to re-do your modeling or analysis as an employee

"actionable guidelines and processes for identifying what consitutes a legitimate
removal request depending on the local norms and regulations of
the requester and data custodian"

---

## Infrastructure for contestation

Note that if you leave `data.csv` on your work machine for all eternity, this breaks contestation! So you need to either have some kind of periodic (weekly?) check-in ritual to see which rows need to be deleted, or you can't actually leave data on your machine and have to "pull" it at training time

---

# Language data specific considerations

## Issues with "Clean Text"

- Idea that some procedure will give you "unbiased" text
- "Noisy social media" vs. "Clean Prestige Text"

See e.g. Anjalie Field, Su Lin Blodgett, Zeerak Waseem, and Yulia Tsvetkov. 2021. A
Survey of Race, Racism, and Anti-Racism in NLP. arXiv:2106.11410 [cs.CL] 

---


## Discussion questions

- How should do you think we should balance training data representation concerns?
- How do we account for the incentives in a product context, where our boss might want our system to be biased towards language or linguistic patterns of a certain market segment?

---

## Property rights and privacy rights

- Data governance framework must account for many definitions of property rights (what does a particularl government say about your right to profit from a piece of artwork, your right to remove it from circulation, etc.)
- Property rights are distinct from privacy rights (require a definition of personal data, typically)

---

## User rights as well?

- Users of models have "user rights" in some jurisdictions as well
- e.g. civil rights in the U.S. context might guarantee non-discrimination from models offered by certain actors (e.g. LLM used in the employment or education context)

(Lots of open questions here, keep an eye on this space.)

---

## This seems like a lot of uncertainty!

- A lot of these points have major caveats like "it depends on jurisdiction" or "courts might decide to enforce a particular interpretation of a particular right"
- This means doing innovative work in this space requires navigating these stormy waters, a bit
- E.g. you might have to hire some folks to handle cross-border user property rights, privacy rights, or user rights if you're building a model in a high-stakes domain

---

## One thing that the ML community can do to help: Dataset documentation

- The Jernite et al. paper also includes a major call for documentation
- Note some potentially really serious issues that have been caught before, e.g. misogyny and very controversial content in computer vision datasets (Birhane et al. ref [19])

---

If you're going into ML research, learning dataset documentation practices may give you a leg up as they become more commonly required in paper submissions.

---


## Existing data management "efforts"

- Centralized (e.g. GitHub, Microsoft Research website)
- Public (e.g. UCI ML, HuggingFace -- things we've used in class

> "Our values of autonomy, consent, and contestation are difficult if not practically impossible for public dataset repositories, due to the full reliance on self-governance by dataset submitters"

---

## Wikimedia as a case study

Wikipedia has a complex governance structure that "works" right now

- rights holders 
- custodians (Wikipedia editors)
- steward (WMF)
- data users / modelers (researchers, e.g.  perhaps you as a student in ML!)

Potential conflicts between values. Many different languages and geographies.

---

## OK, so what should we do?

There's a lot of concepts to unpack here. How should we change our behavior going forward? Assuming we agree with all this, what should we do? If we don't agree with this, what should we do?

---


## Actors

Define 6 actors (they can overlap; you can both host data and use it to train models!)

---

## Data Rights-holders

- either a subject or a creator
- can contest, give consent, express privacy concerns, ask for attribution, ask for just rewards

Example: you put your code on GitHub

---

## Data providers

- organization to aggregates the data

Example: HuggingFace includes your code on Github in "The Stack" based on it's license (and gives you an opt-out option)

---

## Data hosts

- Organization that specifically hosts the data; might be the same as the provider

Example: HuggingFace hosts that data. Perhaps an additional research org, like a lab at a university, also hosts a copy.

---

## Data Modeler

- Organization that does some training!

Example: you train a large language model on a aggregated code data.

---

## Data Stewardship Organization (DSO) and Data helpers

- Organization that facilitates communication between all other actors
- Helpers might be e.g. lawyers who provide advising

Example: This is the org that needs to be brought into existence!

---

## Contractual flow-down

*In this framework*, there's a requirement that:

> "each subsequent actor on this path is responsible for communicating the requirements and restrictions formulated by its predecessors in addition to its own" (Jernite et al., Section 5)

This is part of the proposal: some actors might argue *this isn't currently part of the rules*

---

## Discussion question

- Who stands to gain from contractual flow-down?

---

# CARE principles

[link](https://www.adalovelaceinstitute.org/blog/care-principles-operationalising-indigenous-data-governance/)

CARE = 

- collective benefit
- authority to control
- responsibility
- ethics


## Practice of developing new principles

- Workshop event in 2018
- people come together and draft new set of goals / principles
- drawing on principles from various Data Sovereigny groups (First Nations, Maori, U.S., Torres Strait)

---

## What is "Indigenous data sovereignty"

[link](https://www.lib.sfu.ca/help/publish/research-data-management/indigenous-data-sovereignty)

> "Indigenous data sovereignty means that Indigenous Peoples have the right to own, control, access, and steward data about their communities, lands, and culture"

- Note this a key aspect of Canadian research ethics
- Take a look at above link to learn more about specific examples

---

## Data-centric vs. people-centric

the CARE principles are meant to avoid excessively "Data-centric" approach, and be more people and purpose-driven

Example: Collective Benefit is about the ultimate purpose of the data, not selecting a certain observation from a given data file on the basis of some ML peformance metric

---

## Context: CARE in the previous piece vs. prevailing practice

- Important to note that after having read the Jernite et al. piece, these "people-centric" principles were certainly a part of it. 
- The real contrast here is the current system

---


# Big list of concepts to reflect on

- Values in the ML community
- Lifecycle of data
- Difference between working on a dataset vs. working to get a dataset
- Lifecycle of data

---

- Contestation
- Language discrimination and problematic notions of "clean" data
- Property rights
- Privacy rights

---

- contractual flow-down
- Indigenous data sovereignty
- CARE principles

## Other perspectives

- "Relational theory" from Viljoen [link](https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/ylr131&section=12)