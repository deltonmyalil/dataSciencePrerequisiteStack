import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

A = pd.read_csv("data_1d.csv", header=None).values  # converted the resultant df into matrix

# we need X axis as first column and Y axis as second column in the file data1d.csv
xAxis = A[:, 0]  # ':' means select everything in that dim. so [:,0] means select everything in 0th column
yAxis = A[:, 1]  # [:,1] means select everything in the 1st column


x_line = np.linspace(0, 100, 100)
y_line = 2 * x_line + 1
plt.scatter(xAxis, yAxis)
plt.plot(x_line,y_line)
plt.show()