def calculate_total(prices):
    total = sum(prices)
    return total

def apply_tax(amount):
    tax = (amount*5)/100
    total_with_tax = amount + tax
    return total_with_tax
    