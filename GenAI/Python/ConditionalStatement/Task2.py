order_amount = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discount_order = 0

print("Order Amounts \tDiscount(%)\tFinal Amount")
for amount in order_amount:
    # apply discount rule
    if amount >= 2000:
        discount = 15
    elif amount >= 1500 and amount < 2000:
        discount = 10
    elif amount >= 1000 and amount < 1500:
        discount = 7
    else:
        discount = 0

    # 4. extra : add tax fixed 5 percent and print sub tpta; tax, final total still within 
    # conditionals and basic arithmetic operations
    discount_amount = amount * discount / 100  
    final_total = amount - discount_amount
    total_revenue  = total_revenue + final_total
    if discount > 0:
        discount_order = discount_order + 1
    print(amount,"\t\t", discount, "\t\t", final_total)
print("Total Revenue: ", total_revenue)
#extra
print("Total Orders with Discount: ", discount_order)