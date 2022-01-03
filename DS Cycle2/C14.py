import numpy as np
arr1=np.arange(1,37).reshape((6,6))
print(arr1)
arr2=np.arange(1,10).reshape((3,3))
print(arr2)
a=arr1[0:3,1:4]
print(a)
c=np.multiply(a,arr2)
print(c)
arr1[0:3,1:4]=c
print(arr1)