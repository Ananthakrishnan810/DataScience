import numpy as np
a=np.arange(0,15,2)
print(a)
#1
print("index 2 to 8",a[2:8:2])
#2
print("3 element using negative",a[-3:])
#3
print("last 3 number alternate",a[-5::2])
#4
print(a[-1:-5:-1])