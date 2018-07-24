import pandas as pd

X = pd.read_csv("data_2d.csv", header=None)
# we need to specify header=None as pandas usually assume csv have header row
# print(type(X)) # This function returns a DatFrame datatype

print(X.info())  # Information about the data in df. Also, pandas recognized the float datatype

print(X.head())  # Preview of the first five rows

print(X.head(10))  # Preview of the first ten rows

# X[0][0] does not work as it does in lists/arrays
# We can convert it into a matrix though

M = X.values  # This returns a numpy array. You can check using type(M)

# print(M)  # This prints the entire 2d array of floats
# print(type(M))  # M is of type numpy.ndarray

print(X[X[0] < 5])  # Select all the rows where the data for the zeroth column is less than 5
