import pandas as pd
import numpy as np

# 1. 根據給定的 DataFrame 中取出索引為 3, 4, 8 的 animal 和 age 欄位。
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
print(df.reset_index().loc[[3, 4, 8], ["animal", "age"]])

# 2. 請將 dataFrame 所有字串都變成是大寫開頭。
df = pd.DataFrame([
    ['tom', 'mark', 'mary'],
    ['bob', 'alice', 'john']
])

df = df.applymap(lambda x: str(x).title())
print(df)
