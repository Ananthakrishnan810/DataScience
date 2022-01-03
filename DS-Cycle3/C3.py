import matplotlib.pyplot as plt
import numpy as np

x=np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
y=np.array([173,153,195,147,120,144,148,109,174,130,172,131])
z=np.array([189,189,105,112,173,109,151,197,174,145,177,161])
w=np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.xlabel("Months of year")
plt.ylabel("sale segament")
plt.scatter(x,y,color='pink')
plt.scatter(x,z,color='yellow')
plt.scatter(x,w,color='blue')
plt.show()