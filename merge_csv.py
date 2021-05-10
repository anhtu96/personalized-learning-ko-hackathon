import os
import tqdm
import math
import argparse
import pandas as pd

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
        columns = ['timestamp', 'solving_id', 'question_id', 'user_answer', 'elapsed_time', 'user_id']
    elif dataset_name == 'KT2' or dataset_name == 'KT3':
        columns = ['timestamp', 'action_type', 'item_id', 'source', 'user_answer', 'platform', 'user_id']
    elif dataset_name == 'KT4':
        columns = ['timestamp', 'action_type', 'item_id', 'cursor_time', 'source', 'user_answer', 'platform', 'user_id']

    # user_id_list = []
    print(f'Merging {len(filenames)} .csv files from folder {os.path.join(FOLDER, dataset_name)}...')
    df = pd.DataFrame(columns=columns)
    df.to_csv(f'datasets/{dataset_name}_merged.csv', index=False)
    for fname in tqdm.tqdm(filenames):
        user_id = int(fname.split('.csv')[0][1:])
        f = open(os.path.join(os.path.join(FOLDER, dataset_name), fname), 'r')
        data = f.read().split('\n')
        f.close()
        data = data[1:-1]
        data = [x + ',' +  str(user_id) for x in data]
        # user_id_list += [user_id] * len(data)
        write_data = '\n'.join(data) + '\n'
        with open(f'datasets/{dataset_name}_merged.csv', 'a+') as writer:
            writer.write(write_data)

    # tqdm.tqdm.pandas()
    # df = pd.read_csv(f'{dataset_name}_merged.csv')
    # df['user_id'] = user_id_list
    # df.to_csv(f'datasets/{dataset_name}_merged.csv', index=False)
    print(f'Done! Merged file saved to {os.path.join(FOLDER, dataset_name)}')


def main():
    if args.dataset == 'all':
        for dataset_name in ['KT1', 'KT2', 'KT3', 'KT4']:
            merge(dataset_name)
    else:
        merge(args.dataset)

if __name__ == '__main__':
    main()
