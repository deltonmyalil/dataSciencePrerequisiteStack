import numpy as np

myList = [1, 2, 3]
toArrayArgList = [1, 2, 3]

myList.append(4)  # Append to PythList # Not gonna work with numpyArray
myList = myList + [5]  # Join PythList # Not gonna work with numpyArray,
# + with List is concatenation while the + with numpy array is vector addition
print("After appending 4 and concatenating list with [5]")
print(myList)

list2 = []
for i in myList:
    list2.append(i + i)  # Also not possible in numpyArray
print("After appending i+i from old list to new empty list we get")
print(list2)
print("Using 3*myList on list gives us a concatenated list done three times")
print(3 * myList)

numpyArray = np.array(toArrayArgList)
print("numpyArray is ")
print(numpyArray)
print("appending 4 and 5 to numpy array using numpyArray = numpy.append(numpyArray,[list of elements])")
numpyArray = np.append(numpyArray, [4, 5])
print(numpyArray)
print("After using + on the numpy array as ary+arry, we get vector sum")
print(numpyArray + numpyArray)
print("3*numpyArray gives 3 * each element in np array as follows")
print(3 * numpyArray)

print("Squaring of each elements in a list and numpy array")
print("for list, we have to use for loop with a new array to store the squared values")
squaredList = []
for i in myList:
    squaredList.append(i ** 2)
print(squaredList)

print("for numpy array we simply use numpyArray**2")
print(numpyArray ** 2)
print("taking sqrt using np.sqrt(numpyArray)")
print(np.sqrt(numpyArray))
print("same goes for log")
print(np.log(numpyArray))  # For the above three operations on list, we have to use for loop but on numpy array, you can do directly

