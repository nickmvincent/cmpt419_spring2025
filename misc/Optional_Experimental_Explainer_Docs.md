This semester, I'm experimenting with the use of generative AI to create interactive "explainer docs".

I provide these as examples and encourage you to try this out on your own as well. Part of the value in these comes from reviewing the outputted code, so they're not meant to be "lecture slides".

Also, these are not required content (you don't need to calculate influence estimations by hand, but it can be useful to try!)

Key papers to double check formulas and derivations:
- KL17: https://arxiv.org/abs/1703.04730
- blog walkthrough on logistic regression: https://medium.com/towards-data-science/logistic-regression-from-scratch-870f0163bfc9 (log likelihood, newton method, )
- Pyvdl open source implementation of many estimators: https://pydvl.org/stable/influence/ (see e.g. https://github.com/aai-institute/pyDVL/blob/develop/src/pydvl/influence/influence_calculator.py)
- Hessian of logistic function on SE: https://stats.stackexchange.com/questions/68391/hessian-of-logistic-function
- Derive influence function on SE: https://datascience.stackexchange.com/questions/121608/influence-functions-on-neural-networks-help-with-understanding-of-result-and-de