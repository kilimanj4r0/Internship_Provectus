### Prerequisites
Install the requirements using shell
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

# Solutions to Code Tasks

### SQL
Note that it was tested in `MySQL`.
1. Rewritten SQL query
```sql
 SELECT u.id
 FROM user AS u
 LEFT JOIN departments AS d ON d.user_id = u.id
 WHERE d.department_id != 1 OR d.department_id IS NULL;
```
2. The SQL query to find all duplicate lastnames in a table named **user**
```sql
SELECT lastname
FROM user
GROUP BY lastname
HAVING COUNT(lastname) > 1;
```
3. Write a SQL query to get a username from the **user** table with the second highest salary from **salary** tables. Show the username and it's salary in the result.
```sql
SELECT u.username, s.salary
FROM user AS u
INNER JOIN salary AS s ON s.user_id = u.id
ORDER BY s.salary DESC 
LIMIT 1, 1;
```

### Algorithms and Data Structures
1. Optimised Python code snippet has the `O(n + k)` time complexity due to using dictionary for searching (it is a 
   hashmap, so average time complexity is `O(1)`). The given Python code snippet has `O(nk)` time complexity. 
```python
def count_connections(list1: list, list2: list) -> int:
    count = 0
    ddict = {}
    for el in list1:  # O(len(list1))
        if el not in ddict:  # O(1)
            ddict[el] = 0
        ddict[el] += 1
    for el in list2:  # O(len(list2))
        if el in ddict:  # O(1)
            count += 1
    return count
```
2. The idea is in using dictionary (because of average `O(1)` time complexity for searching) to keep unique elements
and in using `start` and `final` pointers. To detect the maximum length we always should check the difference between
`start` and `final`. Therefore, iterating through the given string, we get that time complexity is `O(n)`, while 
the space complexity is `O(k)` because in worst case we will store in dictionary all unique elements (`k = len(set(s))`)
```python
def find_longest_substring(s):
    ddict = {}  # {char: index}
    max_length = 0
    start = 0
    for final in range(len(s)):  # O(len(s))
        if s[final] in ddict:  # O(1)
            start = max(ddict[s[final]] + 1, start)  # O(1)
        ddict[s[final]] = final 
        max_length = max(max_length, final + 1 - start) # O(1)
    return max_length
```
3. For effective searching for target value in sorted array we usually use the binary search. It provides `O(log n)`
average time complexity.
```python
def find_target_index(num_list, target, left=0, right=None):
    if right is None:
        right = len(num_list) - 1
    mid = (left + right) // 2
    if left > right:
        return left
    if target > num_list[mid]:
        return find_target_index(num_list, target, mid + 1, right)
    elif target < num_list[mid]:
        return find_target_index(num_list, target, left, mid - 1)
    else:
        return mid
```