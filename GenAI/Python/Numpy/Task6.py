import numpy as np

marks = np.array([78,85,90,66,72,88,95,60])

# sorting the marks in ascending order
sorted_marks_asc = np.sort(marks)
# sorting the marks in descending order
sorted_marks_desc = np.sort(marks)[::-1]
# 25th percentile of the marks
percentile_25 = np.percentile(marks, 25)
# 50th percentile of the marks
percentile_50 = np.percentile(marks, 50)
# 75th percentile of the marks
percentile_75 = np.percentile(marks, 75)

#count how may are above average marks
mean_marks = np.mean(marks)
above_average = np.sum(marks > mean_marks)

print("Marks:", marks)
print("Sorted Marks (Ascending):", sorted_marks_asc)
print("Sorted Marks (Descending):", sorted_marks_desc)
print("25th Percentile of Marks:", percentile_25)
print("50th Percentile of Marks:", percentile_50)
print("75th Percentile of Marks:", percentile_75)
print("Number of Students with Above Average Marks:", above_average)
