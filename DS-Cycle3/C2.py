import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array(['mon','tues','wed','thurs','fri'])
y = np.array([300,450,150,400,650])
plt.title("salesdata-1",loc='right')
plt.xlabel("days of week")
plt.ylabel("sales in drink")
plt.subplot(2, 1, 1)
plt.plot(x,y, ls=':',color='c',marker='H',mfc='m',mec='b')
plt.grid()

#plot 2:
x = np.array(['mon','tues','wed','thurs','fri'])
y = np.array([400,500,350,300,500])
plt.subplot(2, 1, 2)
plt.plot(x,y,ls=':',color='y',marker='D',mfc='g',mec='r')


plt.grid()
plt.show()
