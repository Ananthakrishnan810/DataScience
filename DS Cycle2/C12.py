import numpy as np
arr1=np.random.randint(low=2,high=6,size=(2,2))
print(arr1)
#Inverse
iarr1=np.linalg.inv(arr1)
print(iarr1)
#Rank of matrix
rank=np.linalg.matrix_rank(arr1)
print(rank)
#Determinate
de=np.linalg.det(arr1)
print(de)
#transform
tarr1=arr1.flatten()
print(tarr1)
#Eigan
ei=np.linalg.eig(arr1)
print(ei)
