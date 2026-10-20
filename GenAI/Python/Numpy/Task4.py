import numpy as np
data = np.array([[10, 20,30], [40, 50, 60], [70, 80, 90]])

# row-wise sum
row_sum = np.sum(data, axis=1)
# column-wise sum
column_sum = np.sum(data, axis=0)
#minimum value in the array
min_value = np.min(data)
#maximum value in the array
max_value = np.max(data)
#overall sum of the array
overall_sum = np.sum(data)

print("Row-wise Sum:", row_sum)
print("Column-wise Sum:", column_sum)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Overall Sum:", overall_sum)
