def apply_discount(price,percent):
    discount_amount = price * (percent / 100)
    discounted_price = price - discount_amount
    return discounted_price

def flat_discount(price):
    return price - 50