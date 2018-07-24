import numpy as np

# Creating an np 2d array
numpyArrayMatrix = np.array([[1, 2], [3, 4]])

# Same using the list nesting
pythonMatrix = [[1, 2], [3, 4]]

# In python list, to get first element
print(pythonMatrix[0][0])

# Same thing using numpy array
print(numpyArrayMatrix[0][0])

# Also a shorthand notation exists for numpy array
print(numpyArrayMatrix[0, 0])

# However, there is an actual datatype in numpy called matrix
# The official documentation seems to recommend numpy array over matrix
numpyMatrix = np.matrix([[1, 2], [3, 4]])
print(numpyMatrix)
print("Converting numpy matrix to numpy array")
# Directly convert np.matrix to np.array as follows
numpyArrayMatrix = np.array(numpyMatrix)
print(numpyArrayMatrix)

# We can conveniently do operations like transpose by just calling numpyArray.T
print("Transpose is")
print(numpyArrayMatrix.T)