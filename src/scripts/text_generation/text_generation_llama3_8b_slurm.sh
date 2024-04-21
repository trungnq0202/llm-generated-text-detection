#!/bin/bash

#SBATCH --job-name=essay_generation_llama2_13b
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=gpu
#SBATCH --time=06:00:00
#SBATCH --mem=64GB
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --output=myjob.%j.out
#SBATCH --error=myjob.%j.err

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
    --config_path src/config/generation/text_generation_llama3_8b.yaml \
    "

accelerate launch $SCRIPT $SCRIPT_ARGS