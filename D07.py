import numpy as np

# 題目:
array1 = np.array([[10, 8], [3, 5]])

# 1.運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
# ans: 是單位矩陣
array1_inv = np.linalg.inv(array1);
array2 = array1@array1_inv

if np.array_equal(array2, np.array([[1, 0], [0, 1]])):
    print("是單位矩陣")
else:
    print("不是單位矩陣")

# 2.運用上列array計算特徵值、特徵向量?
e, v = np.linalg.eig(array1)
print("特徵值: {}, 特徵向量: {}".format(e, v))

# 3.運用上列array計算SVD?
u, s, vh = np.linalg.svd(array1)
print("u: {}, s: {}, vh: {}".format(u, s, vh))
