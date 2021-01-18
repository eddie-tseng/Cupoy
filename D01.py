import numpy as np

# 1.生成一個等差數列，首數為0，尾數為20，公差為1的數列
arr = np.arange(21)
print(arr)

# 2.呈上題，將以上數列取出偶數
print(arr[0:21:2])

# 3.呈1題，將數列取出3的倍數
print(arr[0:21:3])
