import os
import glob
import pandas as pd


def get_paths_from_dir(dir_name):
    src_data_path = os.path.relpath(dir_name)
    csv_paths = sorted(glob.glob(f'{src_data_path}/*.csv'))
    img_paths = sorted(glob.glob(f'{src_data_path}/*.png'))
    data_quantity = len(csv_paths)
    paths = [[csv_paths[i], img_paths[i]] for i in range(data_quantity)]
    return paths


def combine_data(paths):
    output = pd.DataFrame()
    for path in paths:
        csv_path, img_path = path[0], path[1]
        user_id = os.path.basename(csv_path)[:-4]
        i_df = pd.read_csv(csv_path)
        i_df.insert(0, 'user_id', user_id)
        i_df['img_path'] = img_path
        i_df = i_df.set_index('user_id')
        output = output.append(i_df)
    return output


SOURCE_DATA_DIR = 'src-data'
PROCESSED_DATA_DIR = 'processed_data'
OUTPUT_FILENAME = 'output'

source_paths = get_paths_from_dir(SOURCE_DATA_DIR)
output_frame = combine_data(source_paths)
output_frame.to_csv(f'{PROCESSED_DATA_DIR}/{OUTPUT_FILENAME}.csv')
