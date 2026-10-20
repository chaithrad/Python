import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])

# mean of the marks
mean_marks = np.mean(marks)
# median of the marks
median_marks = np.median(marks)
#variance of the marks
variance_marks = np.var(marks)
#standard deviation of the marks
std_dev_marks = np.std(marks)
#min and max marks
min_marks = np.min(marks)
max_marks = np.max(marks)
# range of the marks
range_marks = max_marks - min_marks

print("Marks:", marks)
print("Mean of Marks:", mean_marks)
print("Median of Marks:", median_marks)
print("Variance of Marks:", variance_marks)
print("Standard Deviation of Marks:", std_dev_marks)
print("Minimum Marks:", min_marks)
print("Maximum Marks:", max_marks)
print("Range of Marks:", range_marks)
