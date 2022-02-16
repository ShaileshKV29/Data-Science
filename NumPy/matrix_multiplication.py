import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([
    [7,8],
    [9,10],
    [11,12]
])

c = np.dot(a, b)
d = a @ b
print(c)
print(d)