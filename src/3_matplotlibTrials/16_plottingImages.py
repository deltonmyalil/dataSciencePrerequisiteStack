import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")  # file has a header
# if it is in another folder outside this, do this read_csv("../anotherFolder/train.csv")
print("read the csv file, and the shape is {0} and size is {1}".format(df.shape, df.size))

M = df.values
image = M[0, 1:]  # Select the 0th row and take every column except the first as it is not a pixel, but a header
# I think it is M[column, row] ie the other way round, need to confirm

print("Shape of image is ", image.shape)  # It is a vector of size 728 in single row

image = image.reshape(28, 28)

print("After reshaping, the image is of shape ", image.shape)

# Now plot the image
plt.imshow(image)  # Optional parameter cmap="gray" to view the image in grayscale
plt.show()

# if you do
# plt.imshow(255-image, cmap='gray')
# then the grayscale image color will be inverted
