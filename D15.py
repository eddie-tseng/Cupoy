import pandas as pd
import matplotlib.pyplot as plt

# 1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
# ans:TAXPTRATIO
df = pd.read_csv('boston.csv')
print(df)
df.boxplot()
plt.show()

# 2. 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
# ans: 負相關
df.plot.scatter(x='NOX', y='DIS')
plt.show()
