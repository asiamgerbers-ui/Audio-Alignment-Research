# RLHF: Understanding in Progress
Introduction: LM are trained by "predicting human text" but this is not really the ultimate goal of AI. "Predict the next word a human would write" versus "Generate the bets quality output possible = totally different goals. What problems are caused by this- Models can make up facts (hallucinate, critical, factual error) and "word choices (minor errors), distributional shift- Model is trained on human written examples and then generates its OWN test-not human text- can cause problems. 

## What Problem Does RLHF Solve?
Improve model responses to they are not "predict a text", but rather quality generating models. Current problems being solved: Models can make up facts (hallucinate, critical, factual error) and "word choices" (minor errors), distributional shift- Model is trained on human written examples and then generates its OWN test-not human text- can cause problems. 

## How Reward Modeling Works
Collect human Preferences (Humans compareL "is summary A or B better?) and build data set of preferences. Reward models learn "When humans prefer summary A over B, what made A better? Then model leanrs "what does 'good' look like. We used RL (reinforced Learning) to train the modes. Use the reward model to score generated summaries, train the big model to maximize the reward score, use PPO algorithm. THEN REPEAT: Get Human Feedback, improve the reward model, improve the policy. 

## Key Ideas So Far
Old way of training AI  models was called supervised learning, which training the models based on human summaries- result = okay summaries. New way of training (RLHF) reinforced learning from human feedback (My job at Alignerr). When implementing RLHF- models work well WITHOUT retraining. Using supervised learning- models required new training on each new domain used. (IE trained on reddit- testing on the news aricles, RLHF-no retraining required on new domain). The goal is not "make better summaries", but ALIGNMENT- Ensuring the AI does what we want. Alignement is CRITICAL for safety as AI gets more and more powerful. 

## Questions I Have
[Write them down...]

## Connection to My Alignerr Work
At Alignerr, we use reinforced learning and reward Modeling to improve client AI systems. I am given DR's (data rows) containing a user prompt followed by the model/assistant (we are training) response. Once everything is read and understood by the human (THAT'S ME!)- we grade/score the model by comparing it to one or more model responses on the same prompt. How did the clients model do comparatively? How can we "train" the client model to Improve it (If it was not rewarded the best model response). We do this by writing Rubrics- Rubrics define what is "good" on a model so we can add, remove, or edit rubrics to improve the model response. Once DR's are updated like this, this data is then returned to the client for them to use to improve their models through re-training. 
```
## THE SAFETY MESSAGE (Last Paragraph - IMPORTANT!)
Read this carefully:
"When misaligned summarization models make up facts, their mistakes are fairly low-risk and easy to spot. However, as AI systems become more powerful and are given increasingly important tasks, the mistakes they make will likely become more subtle and safety-critical..."
---

## Real Implementation of RLHF

I didn't learn RLHF just from papers. I've been implementing it in practice at Alignerr.

### Iteration 1 (Failure Axes Model Testing)
- Collected preferences: Scored models
- Trained reward model: Wrote initial rubrics
- Optimized policy: Models improved from feedback

### Iteration 2 
- Collected NEW preferences: Tested improved models
- Retrained reward model: Edited/improved rubrics
- Further optimization: Models improved again, failures decreased

My rubrics = reward functions
My scoring = preference data
My iteration = policy optimization cycles

My Alignerr work IS RLHF implementation.

This is what real AI safety engineering looks like.
```
## What went Wrong:
Researchers said "we want high-quality summaries" but when labelers evaluated- they got something different. Models looked good to labelers, but not researchers causing a "mismatch". Therefore, RLHF only works if: good feebdack -> good rewrd model -> good policy. Quality = quality good or bad. 

## How do ensure good quality in the future:
For Labelers: Detailed instructions, examples of good vs. bad summaries, explain criteria clearly, make sure we understand the task. Support Labelers: Shared Chat room (Discord), researches answer immediately, clarify confusing cases (edge cases), build shared understanding. Show examples, practice together, give feedback on labeler work (Reviewer), continuously monitor- rates, problems, fixes, and standards. 

## Results
77 out 100 times- labelers agree with researchers. Researchers only agree with each other 73% of the time so 77% is good. Labelers become as good as expert researchers. 

## edge cases:
SItuations where the rules aren't clear. Post is confusing and summary paraphrases it differently. Unclear if paraphrase is accurate. Hard to judge-different labelers may have different opinions. Remember Mismatch between researches and labelers above- Edge cases are where that happens most often. This is what triggers interations. Fairness rubrics will help catch edge case bias. 

## Disadvantages of RLHF
its expensive (who can use this method and at what scale is no longer equal among AI companies) IT can also be used to train models to manipulate people, make people dependent on tech, generate toxic/hurtful content, persuade people with misinformation. Job losses, some data models are exposed to (Like Reddit) can have offensive language, context, bias, and negative stereotypes that can get trained into models, makes good, fair rubrics all the more important. RLHF can be an ethical and social problem. Very difficult to prevent the bad. 