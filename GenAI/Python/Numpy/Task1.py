import numpy as np
# 1D array
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# to create the array without using np.array.
#arr1d = np.arange(1, 11)
print("1D Array:")
print(arr1d)
print("Shape of 1D Array:", arr1d.shape)
print("Data type of 1D Array:", arr1d.dtype)


# 2D array with 3,3 with value s1 to 9
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# to create the array without using np.array
#arr2d = np.arange(1, 10).reshape(3, 3)
print("2D Array:")
print(arr2d)
print("Shape of 2D Array:", arr2d.shape)
print("Data type of 2D Array:", arr2d.dtype)


#numpy array from the list: [10,20,30,40,50]
arrlist = np.array([10, 20, 30, 40, 50])
print("3D Array:")
print(arrlist)
print("Shape of my Array:", arrlist.shape)
print("Data type of my Array:", arrlist.dtype)
print(type(arrlist))
