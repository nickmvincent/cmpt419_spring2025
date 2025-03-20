---
theme: eloc
background: none
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Week 13
mdc: true
author: Prof. Nick Vincent
institute: Simon Fraser University
date: 
---

---

# Perspectives on Data Markets


## Guiding questions

- When are data markets good?
- If data is mostly obtained via markets, do we all need to learn market economics?
- When should we work on systems that are "markets"?
- How should vote or otherwise participate in the governance of market regulations.

---

## Philosophical question

*What's a market to you?*

Question to return to: how might we code a market.

---

## Against individual markets

First paper: 

"Why paying individual people for their health data is a bad idea" - Prainsack and Forgó, 2022

This is a Nature Medicine "comment". Basically, a high-profile op-ed.

---

## Arguments against markets (for health data)

- power asymmetry between subjects + data modelers ("one-way mirror")
- both individual and systemic harms
- exacerbate inequalities 

---

## inequalities in remuneration

- higher income countries get paid more for data
- dependence on data income

---

## data quality issues

- selection bias
- data falsification ("yes, I definitely have that very rare disease...")

---

## Health data as collective property

- individual rights in the context of privacy and consent
- community level decision making
- some tension with open access!

Reflection question: What's health data?

---

## Counterpoints

- Perhaps we should share data to improve patient care, and this might involve markets?
- How much tension is there, really?

---

# Data Sharing Markets: System and Mechanism Design Perspective

Lots of details in the SIGMOD paper -- please peruse based on interests. We won't cover these for the sake of this class.


---

## Acemoglu et al., Too Much Data

> "When a user shares her data with online platforms, she reveals information about others. In such a setting, externalities depress the price of data because once a user's information is leaked by others, she has less reason to protect her data and privacy. These depressed prices lead to excessive data sharing."

See^[https://www.aeaweb.org/articles?id=10.1257/mic.20200200, Acemoglu, Daron, Ali Makhdoumi, Azarakhsh Malekian, and Asu Ozdaglar. 2022. "Too Much Data: Prices and Inefficiencies in Data Markets." American Economic Journal: Microeconomics, 14 (4): 218-56. ]

---

> "We characterize conditions under which shutting down data markets improves welfare. Platform competition does not redress the problem of excessively low data prices and too much data sharing and may further reduce welfare. We propose a scheme based on mediated data sharing that improves efficiency."


## In other words

- Your data sharing choices might affect me
- If you already shared, say, revealing that I'm in this room at 4:30p on Wed., I might share that some info for very low amount
- might need some kind of tax to create better equilibrium

---

## Key goals for 419

- Be aware of these sometimes-competing perspectives
- Be vaguely aware of framing and methods difference between e.g. a Nature editorial, SIGMOD paper, and AEA paper
- Be able to trace the basic arguments, and explain them at a basic level

---

## Example questions

- What are some arguments against individual participation in health care data markets?
- What are some considerations in designing a data sharing market?
- Wbat are some implications of externalities in the context of data sharing?

---

## Additional perspectives for final week

- Data feminism
- Data colonialism

These perspectives may provide arguments for challenging, or changing, certain markets and systems. Again: this is just one of up to 5 (?) courses you may be taking, so the goal is to become aware of these perspectives. Some future classes provide further exploration!

---

## ABMs for structured speculation

Using code (and LLMs, if you like) to explore some of these concepts in a hands on manner