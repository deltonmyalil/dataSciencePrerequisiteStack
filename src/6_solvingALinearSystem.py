import numpy as np

# Form of a linear system of equations is
# AX = B
# Then, multiplying both sides by A^-1 ie inverse of A
# A^-1AX = X = A^-1B
# That is, X = solution = inverseOfA . B ie the dot product of A-inverse and B

# Let the system of linear equations be as follows
# 1x + 2y = 1
# 3x + 4y = 2
# Then,
A = np.array([[1, 2], [3, 4]])
B = np.array([1, 2])
# X = [x,y] ie the variable/unknown matrix

inverseOfA = np.linalg.inv(A)
X = np.dot(inverseOfA, B)  # X is the solution now. However, this method is DISCOURAGED, use numpy.linalg.solve() instead

# Since this is a common operation, np.linalg provides a solve() function.
X = np.linalg.solve(A, B)
print("Solution is", X)
