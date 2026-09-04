#1. use input()
order_amount  = input("Enter the order amount: ")
print(order_amount)
print(type(order_amount))
print(order_amount.isnumeric())
if order_amount.isnumeric():
    order_amount = float(order_amount)
    #2. apply discount rule
    if order_amount >= 2000:
        discount = 15
    elif order_amount >= 1500 and order_amount < 2000:
        discount = 10
    elif order_amount >= 1000 and order_amount < 1500:
        discount = 7
    else:
        discount = 0

    # 4. extra : add tax fixed 5 percent and print sub tpta; tax, final total still within 
    # conditionals and basic arithmetic operations
    discount_amount = order_amount * discount / 100  
    sub_total = order_amount - discount_amount
    tax = (sub_total * 5)/100
    final_total = sub_total + tax
    print(f"Order amount: ${order_amount:.2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Sub Total: ${sub_total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Final Total: ${final_total:.2f}")
else:
    # 3. handle invalid values or order amount
    print("Invalid input. Please enter a numeric value for the order amount.")
  