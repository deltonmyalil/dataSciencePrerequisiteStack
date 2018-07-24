import numpy as np

A = np.array([[1, 2], [3, 4]])
print("Matrix A is:")
print(A)
print()

# inverse of matrix
inverseOfA = np.linalg.inv(A)
print("Inverses of A is:")
print(inverseOfA)
print()

# determinant of A
determinantOfA = np.linalg.det(A)
print("Determinant of A is {0}".format(determinantOfA))
print()

# diagonal elements of matrix
diagonalElementsOfA = np.diag(A)
print("Diagonal elements of A are: {0}".format(diagonalElementsOfA))
print()

# to generate 2x2 matrix of diag elements 1,2,3,4, pass [1,2,3,4] to np.diag
print("generating diagonal matrix")
print(np.diag([1, 2, 3, 4]))
print()

# to generate a 2x2 identity matrix, pass [1,1] to diag
print("Identity matrix of 2x2 dimensions")
print(np.diag([1, 1]))
print()

array1 = np.array([1, 2])
array2 = np.array([3, 4])

# generating outer product
outerProduct = np.outer(array1, array2)
print("outer product is")
print(outerProduct)
print()

# inner product is same as dot product
print("Inner product is {0}".format(np.inner(array1, array2)))
print()

# matrix trace ie sum of diagonals
print("Trace of A is {0}".format(np.diag(A).sum()))
# or use numpy built-in
print("Trace of A through built-in numpy.trace() is {0}".format(np.trace(A)))

# finding eigen values and eigen vectors
print("Eigen values and eigen vectors of A are as follows")
print(np.linalg.eig(A))  # First array shows eigen values, the rest shows eigen vectors
print()

B = np.array([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
print("Matrix B is ")
print(B)
print("Eigen values and Eigen vectors are: ")
print(np.linalg.eig(B)) # First array shows eigen values, the rest shows eigen vectors
print()
