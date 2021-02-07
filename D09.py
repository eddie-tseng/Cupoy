import pandas as pd

# 讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案
data = pd.read_csv('boston.csv', usecols=['CHAS', 'NOX', 'RM'])
data.to_excel('boston.xlsx')
