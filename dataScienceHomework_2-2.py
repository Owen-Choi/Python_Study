import numpy as np
from matplotlib import pyplot as plt

wt = np.random.uniform(40.0, 90.0, 100)
ht = np.random.randint(140, 200, 100)

bmi = wt / (ht * ht)

x = np.arange(100)
plt.scatter(x, wt, color='r')
plt.scatter(x, ht, color='b')
plt.show()