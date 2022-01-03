import numpy as np
#1D
arr1=np.arange(4)
arr2=np.arange(4,10)
print(arr1)
print(arr2)
b=np.append(arr1,arr2)
print(b)
#2D
arr1=np.arange(4).reshape((2,2))
print(arr1)
arr2=np.arange(4,8).reshape((2,2))
print(arr2)
c=np.append(arr1,arr2)
print(c)