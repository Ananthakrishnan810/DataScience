import numpy as np
#vector
A=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
print(A)
B=np.array([3,5,-2])
print(B)
A1=np.linalg.inv(A)
print(A1)
c=np.linalg.solve(A1,B)
print("The vector:")
print(c)