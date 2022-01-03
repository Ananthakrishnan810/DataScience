import numpy as np
#symmetric matrix
arr1=np.arange(1,10).reshape((3,3))
print(arr1)
a=arr1.transpose()
print(a)
c=np.array_equal(arr1, a)
print("The given matrix is symmetric:",c)

b=np.negative(arr1)
d=np.array_equal(a, b)
print("The given matrix is skewsymmetric:",d)