import numpy as np


wt = np.random.uniform(40.0, 90.0, 100)
ht = np.random.randint(140, 200, 100)

ht = ht * 0.01
bmi = wt / (ht * ht)
print(bmi)
