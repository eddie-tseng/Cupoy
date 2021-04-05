import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)
})

df2 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'pine'] * 2,
    'weight': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)
})

# - 依照 fruit 欄位做合併

print(pd.merge(df1, df2, on='fruit'))

# - 依照 index 索引做合併
print(df1.join(df2, lsuffix='_l', rsuffix='_r'))

# [簡答題] 承上題，請問為什麼依照 merge 合併後有些資料不見了？
# ans: default 是 inner join
