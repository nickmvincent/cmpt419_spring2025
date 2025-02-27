## Week 2

The goal of the week 2 readings is to begin getting some exposure to what different researchers mean when they refer to human and data centered ML/AI. We want to start developing some intuiton for when human-centered practices or data-centred thinking might materially change how we design a system, come up with a research question, or deploy a model.

Reading 1: Chancellor 2023.

- Citation: Chancellor, S., 2023. Toward practices for human-centered machine learning. Communications of the ACM, 66(3), pp.78-85.
- About: First, we'll read “Toward Practices for Human-Centered Machine Learning” by Stevie Chancellor, published in the Communications of the ACM. CACM is a venue in which experts in various fields of computing write broad pieces for the entire computing community.
- How to access: Visit https://cacm.acm.org/magazines/2023/3/270209-toward-practices-for-human-centered-machine-learning/fulltext

Reading 2: Mazmunder et al. 2022.

- Citation: Mazumder, M., Banbury, C., Yao, X., Karlaš, B., Gaviria Rojas, W., Diamos, S., Diamos, G., He, L., Parrish, A., Kirk, H.R. and Quaye, J., 2023. Dataperf: Benchmarks for data-centric ai development. Advances in Neural Information Processing Systems, 36, pp.5320-5347.
- About: Second, we'll read the Introduction of the DataPerfs paper, published in NeurIPS 2023 Datasets and Benchmarks Track.
- How to access: Visit https://arxiv.org/abs/2207.10062 
- Notes: You only need to read the Introduction this week.

### Response Instructions:

1) Please write one to two paragraphs describing why you’d like to work on, or with, ML/AI systems? You can imagine these paragraphs as text you might include in a cover letter.
2) Please list 1-3 “domains of interest” (e.g., social media, content recommendation, law, health care, mental health, the environment, economics). They can be at any level of granularity (e.g. “AI for health” is OK, as is “AI for oncology”). Similarly to part 1, the purpose of this is to help me identify trends in your interests so I can suggest optional readings that are of interest to you and your classmates!

If you submit any reasonable formatted submission for this reading response, you'll receive full credit. In future response instructions, you might see something along the lines of, "you must quote on of the readings directly to support your point").

For this reading response, you'll submit via CourSys.

Optional reading

- If interested in data-centric approach to large language models, check out this blog: https://sebastianraschka.com/blog/2023/optimizing-LLMs-dataset-perspective.html 


## Week 3

The goal of the week 3 reading is to gain further exposure to various frameworks put forward around focusing on humans (Schneiderman reading) and/or data (Sambasivan et al reading and Zha et al reading).

Note this week is a bit longer than than Week 2. We'll check in on how it's going, workflow wise, to complete these readings, and focus on challenges that may come up for those who haven't had many reading heavy computing classes previously.

Reading 1: Shneiderman 2020.

- Citation: Shneiderman, B., 2020. Human-centered artificial intelligence: Reliable, safe & trustworthy. International Journal of Human–Computer Interaction, 36(6), pp.495-504.
- About: This is a paper published in the International Journal of Human–Computer Interaction.
- How to access: visit https://www.tandfonline.com/doi/full/10.1080/10447318.2020.1741118 on campus or https://arxiv.org/abs/2002.04087 off campus

Reading 2: Sambasivan et al 2021.

- Citation: Sambasivan, N., Kapania, S., Highfill, H., Akrong, D., Paritosh, P. and Aroyo, L.M., 2021, May. “Everyone wants to do the model work, not the data work”: Data Cascades in High-Stakes AI. In proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (pp. 1-15).
- About: This is a paper published in ACM CHI, the main venue for human-computer interaction research. 
- How to access: visit https://research.google/pubs/everyone-wants-to-do-the-model-work-not-the-data-work-data-cascades-in-high-stakes-ai/

Reading 3: Zha et al 2023.

- Citation: Zha, D., Bhat, Z.P., Lai, K.H., Yang, F. and Hu, X., 2023. Data-centric ai: Perspectives and challenges. In Proceedings of the 2023 SIAM International Conference on Data Mining (SDM) (pp. 945-948). Society for Industrial and Applied Mathematics.
- About: This is a short perspective paper in a data mining conference.
- How to access: visit https://epubs.siam.org/doi/abs/10.1137/1.9781611977653.ch106
- Notes: you should read the short perspective paper. You may optionally also check out the longer survey paper and repo linked here: https://github.com/daochenzha/data-centric-AI


Optional (mainly to give some more examples of academics using human- or data-centric framing):

- https://dl.acm.org/doi/abs/10.1145/3517337
- https://arxiv.org/abs/2311.06703v2
- https://dl.acm.org/doi/10.1145/3544549.3585752

### Response Instructions


Imagine you are a manager at a large tech company tasked with developing a new AI product. You can pick one of the following three options based on your interests, or suggest your own product:

- A large language model that will read physician notes and make suggestions about how to treat patients
- A recommender system for a video-based content app
- A facial recognition system that will be sold via API credits
    
Q1: Thought experiment: Please write 1-2 paragraphs describing how adopting any of the suggestions from any of this week’s readings might change your product features (first define the product). Please directly reference (e.g. directly quote) one or more of the readings.

Q2: Please list three examples of “harms” that might occur from a failure to do “data work” as defined in the Sambasivan reading. You can use the same AI product you picked for Q1, or discuss one or more different AI products. You don’t need to quote the reading directly for this part.

Q3: Quick retrieval question: According to Zha et al., what category would each of the following techniques fall into: feature selection, creating images with randomly occluded patches, using Mechanical Turk to label documents.

Q4: Please let me know roughly how the long the readings and responses took so we can calibrate!


## Week 4

For this week, there will be just two readings. The goal this week is still to gain exposure to all the different frameworks for thinking that motivate "human-centered AI" and "data-centered AI". Last week, we saw several more frameworks, and in particular learned more about specific "data-centric" task formulations.

In our first reading, Chancellor highlighted that human-centered ML is often tied deeply to specific goals around fairness, justice, and values. This week, we'll dive into this with a reading from a textbook.

This week we'll just read two pieces: one is a longer introduction to a fairness in ML textbook, and the other is the Introduction to another research paper.

Please read the Introduction of FairML: https://fairmlbook.org/introduction.html

- While our course material will differ in some ways from a Special Topics course that's entirely focused on fair ML, there's quite a bit of conceptual overlap between being human-centered and trying to achieve some notion of fairness.
- For our purposes, the concept of the "machine learning loop", and especially measurements and going "from data to models" will be highly salient to almost all the topics we discuss, so try to read this one closely! We'll discuss this quite a bit together in class as well.

Please read the Introduction of “Value-Sensitive Algorithm Design: Method, Case Study, and Lessons” by Zhu et al, published in CSCW: https://dl.acm.org/doi/10.1145/3274463 

The goal of this reading is to see another example of how a research project might concretely seek to incorporate values into design. You don't need to read the full paper, though if you're particularly interested in working on algorithm design you might want to!

### Response Instructions:

Q1: Please summarize in your own words the idea of the "machine learning loop". Do your best to capture the key concepts from the FairML intro.

Q2: How does the discussion of feedback loops in FairML Introduction compare to the discussion of feedback in Schneiderman's HCAI? You can just write 2-3 sentences describing major differences or similarities you see. There's not a correct answer here.

Q3: Quick retrieval: What online platform do Zhu et al. use to study value-sensitive design in a real-world setting?

Q4: Please let me know roughly how the long the readings and responses took so I can continue to calibrate!

## Week 5

This week, we are going to start reading a long piece that surveys training data influence:

- Citation: Hammoudeh, Z. and Lowd, D., 2024. Training data influence analysis and estimation: A survey. Machine Learning, 113(5), pp.2351-2403.
- How to access: https://arxiv.org/abs/2212.04612

This piece will represent a large jump from reading about high-level frameworks that consider social factors, incentives, etc. to a much more mathematical framework for thinking about data-centricity. Accordingly, we're going to work through this piece (and some excerpts from the key citations) fairly slowly. For this week, you should just read pages 1-10 (on the arxiv version -- up to Section 4).

For this week's reading responses, you do not need to answer any questions. Instead, please use the reading response as a chance to record any questions that come up (if you want to just ask them in lecture, that's great too!)


## Week 6

This week we will continue reading the Hammoudeh and Lowd survey.

Please read pages 10-21 (up to Section 5.1.2, "Representer Point Methods").

For your response, please answer the following 3 questions:

Q1) Please describe the difference between a leave one out influence value and a Shapley value, in the context of training data influence.

Q2) What is the main issue with calculating retraining-based data values, as described in our reading?

Q3) If you were asked to run a new data market that makes use of influence estimates, which approach from the reading would you use and why? There is no correct answer to question, but you should aim to think through some of the trade-offs.

## Week 7 (Reading Week)

This week, please read: 

- Citation: Hestness, J., Narang, S., Ardalani, N., Diamos, G., Jun, H., Kianinejad, H., Patwary, M.M.A., Yang, Y. and Zhou, Y., 2017. Deep learning scaling is predictable, empirically. arXiv preprint arXiv:1712.00409.
- How to access: https://arxiv.org/pdf/1712.00409.pdf

For your response, please answer the following 3 questions:

Q1) Please describe the consistent finding across all ML domains in this study.

Q2) What are the three "learning regions" that the authors identify?

Q3) About how long did this reading take?

The reading response for this week will be due Week 8 (i.e., two responses due Week 8!)

## Week 8

This week, we're going to start talking about online platforms and their role a key AI training data source. We'll orient much of our discussion around recent advances in Large Language Models, but with the caveat that the core ideas are equally relevant to search, recommendation, and classification systems in many applied domains of interest to our class (e.g. medicine, analytics for sports and games).

First, please read these two short blog posts from 2020 and 2022.

- https://dataleverage.substack.com/p/dont-give-openai-all-the-credit-for
- https://dataleverage.substack.com/p/chatgpt-is-awesome-and-scary-you-deserve-credit


Next, please read Sections 1 and 2 of this pre-print paper:

- https://arxiv.org/abs/2101.00027


For this week, please list three specific online platforms that are useful for AI training.


## Week 9 

Quiz 2 this week + finish project proposal. No required reading. You're encouraged to find reading that supports
your project proposal.


## Week 10

This week, we'll do something a bit different. For your "reading time" (i.e. 1-2 hours, hopefully), you should watch this YouTube video:
https://www.youtube.com/watch?v=zjkBMFhNj_g
If you absolutely are sure you're not interested in Large Language Models, you can use this time to instead find a video or blog post covering your domain of interest.

For your response, please either:
1) Describe one thing from the video that surprised you, or
2) Provide a link to the non-LLM resource you found and describe what you learned from it.


## Week 11

For this week, please read:

First 10 pages of https://arxiv.org/abs/2402.00159

Section 2 of https://dl.acm.org/doi/abs/10.1145/3531146.3534637

Skim this webpage: https://weborganizer.allen.ai/ and look at linked sample data on HuggingFace.

For your response, please:

Describe at a high-level three key components in preparing a high quality pre-training dataset.

## Week 12

Please read the Abstract and Introduction of the following papers. The goal of this set of readings is to get some exposure to different arguments and research directions in the space of data-sharing markets. One reading is from Nature Medicine, one from a data-focused CS conference, and one from an economics journal.

---
Prainsack, B. and Forgó, N. 2022. Why paying individual people for their health data is a bad idea. Nature medicine. 28, 10 (Oct. 2022), 1989–1991.
https://www.nature.com/articles/s41591-022-01955-4


Fernandez, R.C. 2023. Data-Sharing Markets: Model, Protocol, and Algorithms to Incentivize the Formation of Data-Sharing Consortia. Proceedings ACMSIGMOD International Conference on Management of Data (2023).
http://raulcastrofernandez.com/papers/data-sharing-consortia-escrow.pdf

Acemoglu, D. et al. 2022. Too Much Data: Prices and Inefficiencies in Data Markets. American Economic Journal: Microeconomics. 14, 4 (Nov. 2022), 218–256.
https://www.aeaweb.org/articles?id=10.1257/mic.20200200

For your response, describe your planned project and the relevance, if any, of each of these three framings.


## Week 13

The goal of this set of readings is to get some exposure to additional perspectives on data governance.

Read: Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., Holbrook, J., Lovett, R., Materechera, S., ... & Hudson, M. (2020). The CARE principles for indigenous data governance. Data Science Journal, 19, 43-43.
Available as HTML at: https://www.adalovelaceinstitute.org/blog/care-principles-operationalising-indigenous-data-governance/

https://data-feminism.mitpress.mit.edu/pub/vi8obxh7/release/4


For your response, describe your planned project and the relevance, if any, of each of these three framings.