import math_utils
from math_utils import square
import string_utils

# task1
print("Addition:", math_utils.add(5, 3))
print("Subtraction:", math_utils.subtract(5, 3))
print("Square:", square(5))

# task2
print("Capitalized:", string_utils.capitalize_words("happy teachers day"))
print("Reversed:", string_utils.reverse_string("happy teachers day"))
print("Word Count:", string_utils.word_count("happy teachers day"))

#task4
import shop_package.discount as disc
from shop_package.billing import calculate_total
import shop_package.billing

print("Percent Discounted Price: ",disc.apply_discount(1000, 10))
print("Flat Discounted Price: ",disc.flat_discount(1000))

total = calculate_total([100, 200, 300])
print("Total Price:", total)
print("Total Price with Tax:", shop_package.billing.apply_tax(total)) 