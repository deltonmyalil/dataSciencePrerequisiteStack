import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np

R = np.random.random(10000)
plt.hist(R, bins=20)  # by default there are 10 discreet intervals, but you can use parameter bins=20 for 20 intervals
plt.show()
