import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# create data points for x axis
x = np.linspace(0, 10, 50)
# used to generate data, parameters are start point, end point and how many points in between

# for y, create a sin wave
y = np.sin(x)

plt.plot(x, y)
# If the above gives ModuleNotFound, do sudo apt-get install python3-tk
# Note: Works without python3-tk when using ipython console directly
plt.xlabel("Time")
plt.ylabel("Sine function of time")
plt.title("First line graph")

plt.show()  # I think this runs like root.mainloop() in tkinter, need to check
