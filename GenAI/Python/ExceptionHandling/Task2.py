prices = [120,350,'abc',500,-200,800]

total =0

for price in prices:
    try:
        if price < 0:
            raise ValueError("Negative price not allowed.")
        total = total +  price
        print("Running Total",total)
    except TypeError:
        print("SKipping Invalid Price",price)
    except ValueError as ve:
        print("error:", ve)
print("Final Total:", total)
