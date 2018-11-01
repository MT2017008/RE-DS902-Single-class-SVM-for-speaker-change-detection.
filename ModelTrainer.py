import numpy as np
import matplotlib.pyplot as plt
import os
import pickle as pk

#Sample code:

x = np.arange(0, 2 * np.pi, 0.005)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

plt.plot(x, y0)
plt.plot(x, y1)

plt.show()
