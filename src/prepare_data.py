import os
import sys
import string
import random
import argparse
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import preprocess_essay

def generate_random_string(text):
    chars = string.ascii_lowercase + string.digits
    return 'e_' + ''.join(random.choice(chars) for _ in range(8))

def prepare_DAIGT_V2(dir_data: str) -> pd.DataFrame:
    dir_daigt_v2 = os.path.join(dir_data, 'DAIGT_V2/train_v2_drcat_02.csv')
    df_daigt_v2 = pd.read_csv(dir_daigt_v2).rename(columns={'label': 'generated'})
    df_daigt_v2.drop(columns=["RDizzl3_seven"], inplace=True)
    df_daigt_v2["id"] = df_daigt_v2["text"].apply(generate_random_string)
    df_daigt_v2 = df_daigt_v2[["id", "text", "source", "generated"]]
    df_daigt_v2.drop_duplicates(subset=["text"], inplace=True)
    return df_daigt_v2

def prepare_generated_data(dir_data: str) -> pd.DataFrame:
    df_generated = pd.DataFrame()
    dir_generated = os.path.join(dir_data, 'scaling')

    for model in os.listdir(dir_generated):
        dir_model = os.path.join(dir_generated, model)
        df_generated_model = pd.DataFrame()

        for file in os.listdir(dir_model):
            file = os.path.join(dir_model, file)
            df_generated_model = pd.concat([df_generated_model, pd.read_json(file)], ignore_index=True)
            df_generated_model.reset_index()

        df_generated_model["source"] = model
        df_generated = pd.concat([df_generated, df_generated_model], ignore_index=True)
        df_generated.reset_index()
    
    df_generated.rename(columns={"responses": "text"}, inplace=True)
    df_generated["generated"] = 1
    df_generated["id"] = df_generated["text"].apply(generate_random_string)
    df_generated = df_generated[["id", "text", "source", "generated"]]
    df_generated.drop_duplicates(subset=["text"], inplace=True)
    return df_generated

def prepare_daigt_train_test_data(df_daigt_v2: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df_daigt_v2_train, df_test = train_test_split(df_daigt_v2, test_size=0.2, random_state=42)
    return df_daigt_v2_train, df_test


def prepare_data(dir_data: str, dir_output: str):
    df_daigt_v2 = prepare_DAIGT_V2(dir_data)

    # Split DAIGT_V2 data into train and test
    df_daigt_v2_train, df_test = prepare_daigt_train_test_data(df_daigt_v2)

    # Load self generated data
    df_generated = prepare_generated_data(dir_data)
    df_all = pd.concat([df_daigt_v2, df_generated], ignore_index=True)

    print("="*50, "Individual dataset shape", "="*50)
    print("Total DAIGT_V2 essays: ", df_daigt_v2.shape[0])
    print("Total SELF-GENERATED essays: ", df_generated.shape[0])
    print("Total combined essays: ", df_all.shape[0])
    print(df_all[df_all.generated == 0].shape[0])
    print(df_all[df_all.generated == 1].shape[0])


    df_train = pd.concat([df_daigt_v2_train, df_generated])
    print("="*50, "Train/Test dataset shape", "="*50)
    print("Total train essays v1 (DAIGT_V2): ", df_daigt_v2_train.shape[0])
    print("Total train essays v2 (DAIGT_V2 + GENERATED): ", df_train.shape[0])
    print("Total test essays: ", df_test.shape[0])

    print("Preprocessing data...")
    df_daigt_v2_train['text'] = df_daigt_v2_train['text'].apply(preprocess_essay)
    df_train['text'] = df_train['text'].apply(preprocess_essay)
    df_test['text'] = df_test['text'].apply(preprocess_essay)
    
    print("Checking for duplicates...")
    print(df_daigt_v2_train.duplicated().sum())
    print(df_train.duplicated().sum())
    print(df_test.duplicated().sum())

    print(df_daigt_v2_train.duplicated(subset=["id"]).sum())
    print(df_train.duplicated(subset=["id"]).sum())
    print(df_test.duplicated(subset=["id"]).sum())

    print("Saving files...")
    df_daigt_v2_train.to_csv(os.path.join(dir_output, 'train_essays_v1.csv'), index=False)
    df_test.to_csv(os.path.join(dir_output, 'test_essays.csv'), index=False)
    df_train.to_csv(os.path.join(dir_output, 'train_essays_v2.csv'), index=False)
    

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--data_dir', type=str, required=True)
    ap.add_argument('--output_dir', type=str, required=True)

    args = ap.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    prepare_data(args.data_dir, args.output_dir)
