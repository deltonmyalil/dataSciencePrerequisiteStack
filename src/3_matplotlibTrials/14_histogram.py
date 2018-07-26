import matplotlib.pyplot as plt
import pandas as pd

A = pd.read_csv("data_1d.csv", header=None).values

xAxis = A[:, 0]  # A[everything in the 0th column]
yAxis = A[:, 1]  # A[everything in the 1st column]

plt.hist(xAxis)
plt.show()
