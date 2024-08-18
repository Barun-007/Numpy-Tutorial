import numpy as np

a = np.zeros((3,3), dtype = np.int64)
# arr[:] = 4
a.fill(8)
a += 4

print(f"Array A : \n{a}")

b = np.arange(1,10).reshape((3,3))
b = b.astype(np.int64)
print(f"Array B: \n{b}")
print(b.shape)
