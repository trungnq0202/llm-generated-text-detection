#!/bin/bash

#SBATCH --job-name=essay_gen_mistral_7b
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=gpu
#SBATCH --time=08:00:00
#SBATCH --mem=64GB
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --output=jobs_logs/text_gen_mistral_7b.%j.out
#SBATCH --error=jobs_logs/text_gen_mistral_7b.%j.err

######################
### Set enviroment ###
######################
module load cuda/12.1
eval "$(conda shell.bash hook)"
conda activate llm-detect
cd llm-generated-text-detection
# export GPUS_PER_NODE=4
######################

export SCRIPT=src/generate.py 
export SCRIPT_ARGS=" \
    --config_path src/config/text_generation/text_generation_mistral_7b.yaml \
    "

accelerate launch $SCRIPT $SCRIPT_ARGS