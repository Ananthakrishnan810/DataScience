import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Walking", "Cycling", "Car", "Bus", "Train"])
y = np.array([29, 15, 35, 18, 3])

plt.xlabel("mode of transport")
plt.ylabel("frequency")
plt.bar(x,y, color ="#4CAF50", width = 0.1)
plt.show()