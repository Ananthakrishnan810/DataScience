import numpy as np
arr=np.matrix([[3,4,2],[1,5,6],[2,7,5]])
print(arr)
u,s,n=np.linalg.svd(arr)
print(u)
print(s)
print(n)
