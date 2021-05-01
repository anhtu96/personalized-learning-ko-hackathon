import pandas as pd
import os
import tqdm
import math
import argparse

FOLDER = 'datasets'

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='all', help='name of the data, e.g. KT1, KT2, KT3, KT4 or all')

args = parser.parse_args()

def merge(dataset_name):
    """
    Merge all csv files in folder {FOLDER/dataset_name} into 1 csv file.
    """
    filenames = sorted(os.listdir(os.path.join(FOLDER, dataset_name)), key=lambda x: int(x.split('.csv')[0][1:]))
    if dataset_name == 'KT1':
        columns = ['user_id', 'timestamp', 'solving_id', 'question_id', 'user_answer', 'elapsed_time']
    elif dataset_name == 'KT2' or dataset_name == 'KT3':
        columns = ['user_id', 'timestamp', 'action_type', 'item_id', 'source', 'user_answer', 'platform']
    elif dataset_name == 'KT4':
        columns = ['user_id', 'timestamp', 'action_type', 'item_id', 'cursor_time', 'source', 'user_answer', 'platform']
    df = pd.DataFrame(columns=columns)

    print(f'Merging {len(filenames)} .csv files from folder {os.path.join(FOLDER, dataset_name)}...')
    for fname in tqdm.tqdm(filenames):
        user_id = int(fname.split('.csv')[0][1:])
        tmp_df = pd.read_csv(os.path.join(os.path.join(FOLDER, dataset_name), fname))
        tmp_df['user_id'] = user_id
        df = pd.concat([df, tmp_df])
    df.to_csv(f'datasets/{dataset_name}_merged.csv', index=False)
    print(f'Done! Merged file saved to {os.path.join(FOLDER, dataset_name)}')


def main():
    if args.dataset == 'all':
        for dataset_name in ['KT1', 'KT2', 'KT3', 'KT4']:
            merge(dataset_name)
    else:
        merge(args.dataset)

if __name__ == '__main__':
    main()