hdir=$(pwd)

mkdir data

cd data

kaggle competitions download -c llm-detect-ai-generated-text
unzip llm-detect-ai-generated-text.zip -d llm-detect-ai-generated-text
rm llm-detect-ai-generated-text.zip

mkdir persuade_2
kaggle datasets download -d nbroad/persaude-corpus-2
unzip persaude-corpus-2.zip -d ./persuade_2
rm persaude-corpus-2.zip

kaggle datasets download -d thedrcat/daigt-v2-train-dataset
unzip daigt-v2-train-dataset.zip -d ./DAIGT_V2
rm daigt-v2-train-dataset.zip

cd $hdir