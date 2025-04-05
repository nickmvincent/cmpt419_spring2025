---
theme: default
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: "Recap"
mdc: true
---

# CMPT 419: Human-Centered and Data-Centric AI

## Spring 2025 Course Recap in 20 minutes

### Aka: did this course have any content in it, or is the professor just a very fast talker?
Prof. Nick Vincent, Simon Fraser University

---

## Course Overview

This course explored the intersection of human values and data practices in AI systems through four key modules:
1. **Frameworks for Human-Centered & Data-Centric AI**
2. **Data Valuation & Scaling**
3. **Online Platforms & Content Ecosystems**
4. **Data Governance, Markets & Voting**

---

## Module 1: Frameworks for HCAI & DCAI

### Human-Centered Machine Learning (Chancellor 2023)
- **Definition**: "A set of practices for building, evaluating, deploying, and critiquing ML systems that balances technical innovation with an equivalent focus on human and social concerns"
- **Key Practices**:
  - Question if ML is the right solution
  - Acknowledge researcher positionality
  - Consider broader human ecosystems beyond users
  - Collaborate with domain experts
  - Anticipate and iterate on sociotechnical failures

### Human-Centered AI (Shneiderman)
- Emphasizes **Reliable, Safe & Trustworthy** systems
- Balances human control with computer automation
- Considers spectrum of criticality in different applications

---

## Module 1: Frameworks (Continued)

### Data-Centric AI
- Shift focus from model architecture to data quality
- Examples: parsing, augmentation, selection, quality assessment, acquisition, cleaning

### Data Cascades (Sambasivan et al.)
- Highlighted how data quality issues accumulate through the ML pipeline
- Emphasized importance of domain expertise in data labeling
- Connected data practices to global equity issues

### Value-Sensitive Algorithm Design
- Incorporates stakeholder values into algorithm design process
- Builds on user-centered design, value-sensitive design, and participatory design traditions

---

## Module 1: The ML Learning Loop

A framework for understanding different intervention points for HCAI:

1. State of the world
2. Measurement → Data
3. Learning → Model
4. Predictions → Impact on subjects
5. Return to state of the world

Each stage offers different opportunities for human-centered approaches and ethical considerations.

---

## Module 2: Data Valuation and Scaling

### Training Data Influence (Hammoudeh & Lowd 2023)
Four key approaches to measuring data influence:

1. **Leave-One-Out (LOO) Influence**: Remove an instance and measure change in risk
   - Simple but extremely expensive: O(nT) complexity

2. **Downsampling**: Train ensemble of submodels on data samples
   - More efficient than LOO but still costly
   - Provides consistent LOO estimates with tunable parameters

---

## Module 2: Data Valuation (Continued)

3. **Shapley Values**: Game theory approach to data valuation
   - Considers all possible subsets of training data
   - Exponential complexity but strong theoretical guarantees
   - Properties: null player, symmetry, linearity, Pareto optimality

4. **Influence Functions**: Gradient-based approximation
   - Uses Taylor series approximation
   - no retraining
   - Requires model differentiability and convexity assumptions
   - Much faster but less accurate
   - We read some ``old'' work, but recent work applies to LLMs!

---

## Module 2: Data Scaling Laws

### Empirical Findings (Hestness et al.)

- Power law relationship between dataset size and model performance
  - Generalization error: ε(m) ∝ αm^β_g 
  - β_g ranges from -0.07 to -0.35 in practice (not -0.5 as some theory suggests)

- Three regions of scaling:
  - Small training set region (random guessing)
  - Power law scaling region (where most work happens)
  - Irreducible error region ("flat zone")

- Relationship to training data influence: both examine counterfactual worlds where data availability differs

---

## Module 3: Online Platforms & Content Ecosystems

### AI Training Data Sources
- **The Pile**: Early influential dataset showing importance of diverse sources
  - Top sources: Common Crawl, PubMed Central, Books3, OpenWebText2, arXiv
  - Used multiple "epochs" for high-quality sources like Wikipedia

### Wikipedia's Role in AI
- Used as direct knowledge source (answering queries)
- Critical training data for many foundational models
- Source of labeled data in training pipelines (e.g., ImageNet)
- Example of platform design affecting data quality

---

## Module 3: Platform Design & Data

### Platform Design Choices Impact Training Data
- Design features that affect data collection (upvotes, likes, etc.)
- Platform norms and governance determine what content exists
- Example: Wikipedia's "Good" and "Featured" article criteria used in dataset filtering

### User-Generated Content (UGC)
- Platforms like Reddit, GitHub, StackExchange provide valuable training data
- Platform design directly impacts AI capabilities
- User actions (votes, shares) frequently used as quality signals

---

## Side note: Large Language Model practicals

### LLM Core Components (Karpathy)
- Parameters file (~140GB for 70B model)
- Execution code (~500 lines)
- Training process:
  - Pretraining: ~10TB text, 6000 GPUs, ~$2M cost
  - Fine-tuning: ~100K high-quality examples, much cheaper

### LLM Data Pipeline
Multiple stages of data processing:
- Collection → Filtering → Deduplication → Quality assessment
- Language-specific filtering → Topic filtering → Safety filtering

---

## Module 4: Data Markets & Governance

### Data Governance for LLMs (Jernite et al.)
- Proposed Data Stewardship Organizations (DSOs)
- Considers lifecycle: creation, selection, documentation, dissemination, etc.
- Defines responsibilities across stakeholders:
  - Rights-holders, providers, hosts, modelers, DSOs, helpers
- Emphasizes contestation and contractual flow-down

### CARE Principles for Indigenous Data Governance
- **C**ollective benefit
- **A**uthority to control
- **R**esponsibility
- **E**thics

---

## Module 4: Data Markets

### Perspectives on Data Markets
- **Against individual markets** (Prainsack & Forgó)
  - Power asymmetry between subjects and modelers
  - Risk of exacerbating inequalities
  - Health data as collective property

- **Economic analyses** (Acemoglu et al.)
  - Data sharing externalities depress prices
  - Privacy interdependence creates market inefficiencies
  - Platform competition may not solve these issues

---

## Key Questions for Reflection

1. When should we apply human-centered vs data-centric approaches?
2. What are the different points of intervention in the ML pipeline?
3. How should we value training data contributions?
4. What governance frameworks will shape AI development (and how will this affect your job?). What should we do?
5. How can we balance open research with proper compensation and consent (and how will this affect your job?)?

---

## Thank you!

CMPT 419: Human-Centered and Data-Centric AI
Spring 2025