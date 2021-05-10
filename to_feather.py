import datatable as dt
import os

FOLDER = 'datasets'
file_list = ['KT3_merged.csv', 'KT4_merged.csv']
def convert_to_feather(fname):
    df = dt.fread(fname).to_pandas()
    df.to_feather(fname.split('csv')[0] + 'feather')
    del df


if __name__ == '__main__':
    for f in file_list:
        convert_to_feather(os.path.join(FOLDER, f))