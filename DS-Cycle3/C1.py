import numpy as np
from matplotlib import pyplot as pt
x=np.arange(2001,2008)
y=np.array([24000,22500,19700,17500,14500,10000,5800])
pt.title('Value Depreciation' ,loc='left')
pt.xlabel("year")
pt.ylabel("car Value")
pt.plot(x,y, ls='-.',c='r',marker='*',ms=20,mfc='g',mec='g')
pt.show()