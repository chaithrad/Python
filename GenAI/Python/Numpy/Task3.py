import numpy as np

values = np.array([2,4,6,8,10])
# square of the values
squared_values = np.square(values)
#exponential of the values
exponential_values = np.exp(values)
# natural logarithm of the values
logarithm_values = np.log(values)
#sum of the values
sum_values = np.sum(values)
#cumulative sum of the values
cumulative_sum_values = np.cumsum(values)

print("Original Values:", values)
print("Squared Values:", squared_values)
print("Exponential Values:", exponential_values)
print("Logarithm Values:", logarithm_values)
print("Sum of Values:", sum_values)
print("Cumulative Sum of Values:", cumulative_sum_values)
    