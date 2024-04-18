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

