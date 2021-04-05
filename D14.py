import pandas as pd
import numpy as np

df1 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv'
)
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv',
    keep_default_na=True,
    na_values=['na', '--']
)

# 1. [簡答題] 比較下列兩個讀入的 df 有什麼不同？為什麼造成的？
# ans: 把'na', '--'視為缺失值轉換成NaN

import requests

r = requests.get('https://www.dcard.tw/_api/forums')
response = r.text

import json

data = json.loads(response)
df = pd.read_json(data)
df.sort_values('subscriptionCount')
df.to_csv('./D014.csv')
