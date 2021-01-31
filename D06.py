import numpy as np
# 1.將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open('multi_array.npz', 'wb') as f:
    np.savez(f, array1=array1, array2=array2)

# 2.讀取剛剛的npz檔，加入下列array一起存成新的npz檔

npz_file = np.load('multi_array.npz')

with open('multi_array2.npz', 'wb') as f:
    np.savez(f, array1=npz_file['array1'], array2=npz_file['array2'], array3=np.array(range(10)))

