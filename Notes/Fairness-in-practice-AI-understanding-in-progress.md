## The core problem in plain language:
Most fairness research assumes you have complete data — you know the outcome for everyone in your dataset. But in the real world, data is often censored, meaning you simply don't know what happened to some people yet. This section argues that ignoring that creates a serious blind spot.

## Two types of censorship described:
Administrative censoring — the study just ended before the person experienced the event (they might still experience it later)
Loss to follow-up — the person dropped out, withdrew, or had a competing event happen first

## Why this matters for fairness specifically:
Here's the tension worth sitting with: if you drop censored observations (common practice), or ignore the censorship information, you're making assumptions that could affect demographic groups differently. Imagine a clinical trial where one group is more likely to drop out — discarding their data silently skews your model.
The real-world stakes they gesture at:

COMPAS (recidivism prediction) — already controversial for racial bias
KKBOX (customer churn in marketing)
Clinical outcome prediction

// NOTE: A question worth reflecting on: The authors say existing fairness notions are "hindered" by assuming class labels are always present. Can you think of why censored data might introduce different kinds of unfairness than what standard fairness metrics would catch?  A: Incomplete data forces the model to make assumptions — and those assumptions are where bias and unfairness sneak in. That's precisely the problem the authors are describing.

## Concordance Imparity (CI) — Group Fairness
The core question CI asks is: does the model perform equally well at ranking outcomes across demographic groups?

## It works in two steps:
At the individual level — does the model correctly order pairs of people by their survival time?
At the group level — is that ordering ability consistent across groups, or does it systematically fail for certain populations?

## A lower CI score = a fairer model. The key innovation here is that it explicitly uses survival time and censorship information rather than ignoring it.
Fair Discounted Cumulative Gain (FDCG) — Individual Fairness
FDCG asks: if two people are similar going in, are they treated similarly coming out?

## It builds two ranking lists:
One based on similarity in the input space (similar people)
One based on similarity in the output space (similar predictions)

// NOTE: If those lists don't match, someone is being treated unfairly.

## Fair Survival Random Forests (FSRF) — Group Debiasing
FSRF modifies how a Random Forest makes its splitting decisions. Normally a tree splits data to maximize predictive accuracy. FSRF adds a fairness consideration through the Fair Survival Difference (FSD) criterion, which essentially asks:
Does this split improve prediction AND reduce discrimination at the same time?
The clever design detail: when a candidate split has zero discrimination (CI = 0), FSD becomes positive infinite — meaning the algorithm strongly prioritizes splits that are already fair.
## At Alignerr, I implement fairness debiasing similar to FSRF's methodology. Rather than retraining from scratch, I add fairness constraints (rubrics) to existing neural networks. Each iteration provides new ranking data, allowing the system to improve fairness while maintaining the base model's predictive power. This approach prioritizes both interpretability and efficiency—critical in production systems."


## Individual Fair Survival (IFS) — Individual Debiasing
IFS is built on top of DeepSurv, a neural network. Its innovation is framing individual fairness as a ranking consistency problem rather than relying on the notoriously difficult Lipschitz condition.
The loss function penalizes the model when similar people going in get ranked inconsistently coming out — and it does this jointly with the prediction objective.
## The paper shows:
FSRF = fairness debiasing approach (originally designed for Random Forests)
IFS = the SAME fairness debiasing approach (adapted for Neural Networks)

## What you're doing at Alignerr:
Taking FSRF-like methodology (fairness constraints + iterative improvement)
Applying it to neural networks (like IFS does).
FSRF is the foundational IDEA/methodology
IFS is the adaptation of that idea to neural networks
You're doing something similar (FSRF methodology applied to neural networks)
## The paper describes FSRF and IFS as two implementations of fairness debiasing: FSRF for Random Forests, IFS for Neural Networks. At Alignerr, I apply similar fairness debiasing principles to existing neural network models. Rather than building new systems, I layer fairness constraints (rubrics) onto production models, allowing them to improve fairness iteratively—much like IFS, but through human feedback ranking rather than a neural loss function."

## WHY WOULD THEY USE DEEPSURV VERSUS STARTING FROM SCRATCH:
Scientific isolation — By keeping the base model constant, any fairness improvement can be attributed specifically to the new loss function. If they built from scratch, you couldn't tell if improvements came from the fairness component or just better architecture. Established models like DeepSurv means the bias is already baked in — just like real-world deployed models. If IFS can debias that, it demonstrates the approach works under realistic conditions, not just in a clean experimental environment. That's stronger evidence.
Practical adoption — Practitioners already using DeepSurv don't have to rebuild everything. They can add the fairness layer on top. This matters enormously in real healthcare settings.
Credibility — DeepSurv is widely validated. Building on it means the survival prediction component is already trusted.
Controlled environment" — That's precisely the scientific term for it. You isolated the variable being tested (the fairness loss function) while keeping everything else constant. That's rigorous experimental design.
Cost efficiency — Yes, absolutely. And this connects back to something you said earlier about RLHF being expensive and not accessible to all companies. The same logic applies here. Building fairness solutions that work on top of existing infrastructure lowers the barrier to adoption significantly. A hospital using DeepSurv doesn't need a research budget to implement IFS.
Unknown unknowns — This is actually the most sophisticated point you just made. You're essentially saying:
We know what problems exist in DeepSurv. A brand new system would introduce problems we haven't encountered yet and aren't prepared for.

## Specifically what assumption the model makes when it ignores censored data? And why that assumption hurts different groups differently?
Think about it this way:
If you DROP all censored observations, what demographic group might you be silently removing more of?
What if one group is more likely to have "loss to follow-up"?
What does the model learn if it's trained on a biased subset of the data?

EXAMPLES: Imagine a clinical trial predicting heart disease outcomes:
Scenario 1 (Ignoring censorship):
100 people enrolled
30 are still being monitored (censored — we don't know their outcome yet)
You DROP those 30 people
Model trains on only 70 people
But here's the unfairness:   What if those 30 people who dropped out are disproportionately from one demographic group?
Example: Women more likely to drop out due to work/family responsibilities.  Now your model trained on mostly men.  The model learned "heart disease patterns in men," not "heart disease patterns in all people".  The bias isn't stereotypes. It's sampling bias.

## Most likely to be censored (dropped out/loss to follow-up):
Groups with fewer resources (can't afford to stay in study)
Groups with language barriers (harder to follow protocol)
Groups with less medical trust (historical trauma with healthcare)
Groups with less access (transportation, time off work)

## When they're removed from training data:
The model becomes optimized for the people who COULD stay
It's less accurate for the people who DROP OUT
Which is the marginalized group

That's the unfairness. 💙

## THE FAIRNESS TRAP
Standard approach (ignores censoring):
Drop all people with censored outcomes
↓
Dataset is now overrepresented by people who stayed
↓
If Group A withdraws more → Group A is underrepresented
↓
Model learns on skewed data
↓
Model makes biased predictions
What fairness metrics miss:
They look at final outcomes. But they never see the PEOPLE WHO WERE REMOVED by ignoring censoring.

1. Why survival analysis specifically?
You understood WHAT censored data is
But do you understand WHY this paper focuses on survival/censored data contexts?
What domains use this? (Healthcare, criminal justice, employee retention, product lifetimes, etc.)
Why is fairness in survival analysis important NOW?
## This paper embarks on a comprehensive review of recent advances in AI fairness, with a specific focus on bridging these conceptual and practical gaps for the effective deployment of fairness-enhancing techniques in real-world scenarios. By critically evaluating the latest developments in AI fairness, this review seeks not only to identify existing gaps but also to propose innovative solutions that reconcile the theoretical underpinnings of fairness with the complex realities of real-world data dynamics.

## Existing fairness literature assumes static, complete data in supervised settings. But real-world data exhibits censoring (incomplete outcomes), temporal evolution (data changes over time), and non-IID structures (interconnected relationships). This paper addresses that gap—fairness can't work in practice if it ignores these realities. At Alignerr, I encounter all three: incomplete labeling, iterative model improvement, and diverse interconnected data types. This paper's approach is directly applicable."
 ## RELATED TO ALIGNERR: Your rubric work encounters exactly this:
Censoring: Labelers withdraw or tasks remain incomplete → missing outcomes
Evolution: V1 → V2 iteration means data dynamics change
Non-IID: Different types of inputs (accents, speakers, audio contexts) aren't independent
If you ignore these, your fairness rubrics miss bias in those exact places.



3. The paper presents two metrics for censored fairness: Concordance Imparity (group-level) and FDCG (ranking perspective). While both are theoretically sound, the paper provides no guidance on when to use each. In practice, the choice depends on whether your concern is group-level bias or individual ranking consistency. At Alignerr, we focus on group fairness across demographic groups—suggesting Concordance Imparity would be most applicable to our rubric validation work."

4. "Fairness research and real-world practice are MISALIGNED"
"Recent work is trying to FIX that alignment"
"This paper catalogs those fixes and shows what's possible".  A review of advances bridging the gap between fairness theory and real-world deployment

5. (new!): "Intersectionality gap: Even as we fix bias, we might harm people at the intersection of multiple marginalized identities. This means fairness work needs to be holistic, not piecemeal."