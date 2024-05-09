# LLM-generated text detection - Student essays
This is the GitHub repo for the **CS6120: Natural Language Processing**'s final project. The goal is to build a machine-learning model that can detect whether an essay is written by a student or AI-generated, which is based on a recent Kaggle competition: [LLM - Detect AI Generated Text](https://www.kaggle.com/competitions/llm-detect-ai-generated-text). Refer to the following sections for the solution's summary, model training code, and hardware specifics.

## Dataset
* [Competition dataset](https://www.kaggle.com/competitions/llm-detect-ai-generated-text/data)

* [DAIGT_V2 dataset](https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset) (including original competition's dataset)

* [PERSUADE corpus](https://www.kaggle.com/datasets/nbroad/persaude-corpus-2)

**Classes mapping**

|  Class | Numeric label|
|---|---|
| Human written essays  | 0 |
| LLM-generated essays  | 1 |

## Our approach
![Data augmentation pipeline](imgs/data_augmentation_pipeline.png)

To improve our model generalization capability, we proposed a small pipeline for augmenting our dataset. Specifically, we  instruction tune 6 LLMs on the [PERSUADE corpus](https://www.kaggle.com/datasets/nbroad/persaude-corpus-2) which were then used for generating essays. The final dataset includes:
* 80% DAIGT_V2 (~36.000 essays)
* ~13.000 essays generated from our finetuned LLMs including: mistral_7b, falcon_7b, opt_125m, llama3_8b, gpt2, and llama2_13b

This results in a total of **~50.000 essays** for training, and **~9.000** for validation.


![Data augmentation pipeline](imgs/datasource_distribution.png)




## Section 1: Setup
## Section 2: Training




