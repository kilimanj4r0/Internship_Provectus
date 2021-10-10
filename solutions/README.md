### Prerequisites
```shell
pip install -r requirements.txt
```

## Level 1

### Files definitions:

- src_data - Path with source data needed to be processed.
- processed_data - Path with output processed data.

`output.csv` file contains next columns:

1. user_id - User id
2. first_name - User first name
3. last_name - User last name
4. birthts - User birthdate timestamp in milliseconds UTC
5. img_path - Relative path of user image 

**For example:**

```text
user_id,first_name, last_name, birthts,img_path
1000,Susan, Lee,612302400000,src-data\1000.png
```

### How does the script `level_1.py` work:
We
1. Define constants of directory names (`SOURCE_DATA_DIR`, `PROCESSED_DATA_DIR`) and output filename (`OUTPUT_FILENAME`)
2. Read paths of `.csv` and `.png` files needed to combine using function `get_paths_from_dir(dir_name)`
3. Combine the given data into the one `pandas.DataFrame` iterating over all paths:
   1. Get `user_id` from filename
   2. Create the temp `pandas.DataFrame` reading the `i`-th `.csv` file
   3. Insert the `user_id` column in the beginning with the value of `user_id`
   4. Insert the `img_path` column in the end with the given image path
   5. Change index column of temp `pandas.DataFrame` to `user_id` column
   6. Append the row with `i`-th user data to output `DataFrame`
4. Store the output `pandas.DataFrame` as the `output.csv` file

Note that duplicates will always be overwritten since the script makes the `output.csv` file based on the files of
source data directory.
