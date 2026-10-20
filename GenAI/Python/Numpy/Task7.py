import numpy as np

sales = np.array([1200,1500,900,2000,1800,1700,1600])
# total weekly sales
total_sales = np.sum(sales)
# avergae daily sales
average_sales = np.mean(sales)
# highest and lowest sales
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
# std deviation of sales
std_dev_sales = np.std(sales)
# identify days with sales above average
above_average_days = np.sum(sales > average_sales)

#Identifying specific days/values above average using boolean indexing (e.g., sales[sales > avg] or np.where)
#above_average_values = sales[sales > average_sales]
#np.where(sales > average_sales)  # returns the indices of days with sales above average
#print(np.where(sales > average_sales))

print("Total Weekly Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Standard Deviation of Sales:", std_dev_sales)
print("Days with Sales above Average:", above_average_days)