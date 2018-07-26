import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")  # file has a header
# if it is in another folder outside this, do this read_csv("../anotherFolder/train.csv")
print("read the csv file, and the shape is {0} and size is {1}".format(df.shape, df.size))

M = df.values

