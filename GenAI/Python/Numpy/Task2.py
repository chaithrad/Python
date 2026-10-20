import numpy as np

A = np.array([10,20,30,40])
B = np.array([1,2,3,4])
added_array = A + B
print("Added Array:", added_array)

subtracted_array = A - B
print("Subtracted Array:", subtracted_array)

multiplied_array = A * B
print("Multiplied Array:", multiplied_array)

divided_array = A / B
print("Divided Array:", divided_array)

powered_array = A ** 2
print("Powered Array:", powered_array)

# using numpy functions
added_array_func = np.add(A, B)
print("Added Array using function:", added_array_func)

subtracted_array_func = np.subtract(A, B)
print("Subtracted Array using function:", subtracted_array_func)

multiplied_array_func = np.multiply(A, B)
print("Multiplied Array using function:", multiplied_array_func)

divided_array_func = np.divide(A, B)
print("Divided Array using function:", divided_array_func)

powered_array_func = np.power(A, 2)
print("Powered Array using function:", powered_array_func)