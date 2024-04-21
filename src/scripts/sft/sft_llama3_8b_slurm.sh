#!/bin/bash

#SBATCH --job-name=essay_generation_gpt2
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=gpu
#SBATCH --time=08:00:00
#SBATCH --mem=64GB
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --output=myjob.%j.out
#SBATCH --error=myjob.%j.err

######################
### Set enviroment ###
######################
module load anaconda3/2022.05 cuda/12.1
# conda activate llm-detect
cd llm-generated-text-detection
# export GPUS_PER_NODE=4
######################

export SCRIPT=src/instruct.py 
export SCRIPT_ARGS=" \
    --config-name instruct_sft_llama3_8b \
    use_wandb=false
    "

accelerate launch $SCRIPT $SCRIPT_ARGS