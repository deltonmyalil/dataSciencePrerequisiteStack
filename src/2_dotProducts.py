import numpy as np

# let there be two vectors a = [1,2] and b = [2,1]

a = np.array([1, 2])
b = np.array([2, 1])

dotProduct = 0
for e, f in zip(a, b):
    dotProduct += e * f
print("dot product is {0}".format(dotProduct))

print("row wise corresponding product is {0}".format(a * b))  # will only work with arrays of same size

print("sum of the array elements of A is given by np.sum() as {0}".format(np.sum(a)))
# the above is also equivalent to a.sum() as it is an instance method

# if you get the sum of all elements of row wise product, you get dot product, hence do the following
print("dot product of a and b through np.sum(a*b) is {0}".format(np.sum(a * b)))

# np also provides built-in np.dot() function
print("dot product using built-in np.dot(a,b) is {0}".format(np.dot(a, b)))
# the above is same as a.dot(b), also b.dot(a) as it is an instance method of numpy array

# Now let us calculate the angle between vectors a and b
# For this we need to first calculate the length(magnitude) of the vector
# length is the square root of the sum of squares of each element ie root(a^2 + b^2)
print()
aMagnitude = np.sqrt(sum(a * a))
print("Magnitude of a is {0}".format(aMagnitude))
bMagnitude = np.sqrt(sum(b * b))
print("Magnitude of b is {0}".format(bMagnitude))
# numpy has numpy.linalg.norm() to do this - ie finding magnitude of vector
print("Magnitude of a through np.linalg.norm(a) is {0}".format(np.linalg.norm(a)))
print("Magnitude of b through np.linalg.norm(b) is {0}".format(np.linalg.norm(b)))
# now we got magnitude of both vectors. We can calculate the cos of angle as a.b = |a||b|cosTheta
cosTheta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("Cosine of the angle between a and b is {0}".format(cosTheta))
theta = np.arccos(cosTheta)  # np.arccos() is the inverse cos function which returns angle in radian
print("Hence the angle between the vectors is inverse Cos, which is {0} radian".format(theta))
