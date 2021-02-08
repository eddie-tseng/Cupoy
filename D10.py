import pandas as pd

# 題目:
# 讀取STOCK_DAY_0050_202009.csv串聯STOCK_DAY_0050_202010.csv，並且找出open小於close的資料
stock_data1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock_data2 = pd.read_csv('STOCK_DAY_0050_202010.csv')
stock_data = pd.concat([stock_data1, stock_data2], axis=0)
print(stock_data[(stock_data.open) < (stock_data.close)])
