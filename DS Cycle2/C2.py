import numpy as np
arr=np.array([[1,3,5],[2,4,6]], dtype='complex')
print(arr)
print('shape of the array:',arr.shape)
print('The dimension of the array',arr.ndim)
narr=arr.reshape(3,2)
print('reshape of the array\n',narr)