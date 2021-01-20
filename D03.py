import numpy as np

# 1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?

V1 = 20000
V0 = 20
print(20*np.log10(V1/V0))

# 2.30分貝的聲壓會是50分貝的幾倍?

print(np.power(10, 30/20)/np.power(10, 50/20))
