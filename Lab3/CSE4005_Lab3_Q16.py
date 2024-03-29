# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q16] Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame
import numpy as np
import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
df.loc['k'] = ['dog', 4, 2, 'yes']
print("DataFrame after appending row 'k':")
print(df)
df = df.drop('k')
print("\nOriginal DataFrame after deleting row 'k':")
print(df)
