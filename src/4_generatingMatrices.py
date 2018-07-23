import numpy as np
# from random import randint

# Creating an array of zeroes. Note: array by default refers to numpy array
Z = np.zeros(10)
print(Z)

print()

# For a 2D array of all 0s
Z = np.zeros((10, 10))  # The function still takes one parameter - a tuple containing both dimensions
print(Z)

print()

# For a 2D array of all 1s
O = np.ones((10, 10))
print(O)

# For a 2D random array of size 10x10
R = np.random.random((10, 10))
print(R)
# The  elements will be between 0 and 1

print()

# For a 2D random gaussian distributed numbers we use randn, but it takes arguments differently
G = np.random.randn(10, 10)  # Note that unlike random(), randn() takes multiple args and not a tuple
print(G)
# These numbers will be in gaussian distribution with mean 0 and variance 1

# There are function to calculate central tendencies
print("Variance using numpyarray.var() is {0}".format(G.var()))
print("Mean using numpyarray.mean() is {0}".format(G.mean()))

print()

# making 10x10 matrix of random elements between 0 and 9 (both included)
randomMatrix = np.random.randint(0,10, size=(10, 10))
print(randomMatrix)
