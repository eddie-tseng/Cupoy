import numpy as np

# 1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充
array1 = np.array(range(30))
array1 = array1.reshape((5, 6), order='F')
print(array1)

# 2.呈上題的array，找出被6除餘1的數的索引
print(np.where(array1 % 6 == 1))
