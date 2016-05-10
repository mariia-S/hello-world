# Calculate profit

products = []
def add_product (product, qty, plant_price):
    products.append ([product, qty, plant_price])
    return products
    
def add_initial_money (money):
    return money

def calculate_qty(needed_profit, product_price, ingridient_price):
    product_qty = needed_profit/(product_price - ingridient_price)
    return product_qty

print calculate_qty (500, 50, 2+3)

print add_product ("tomato", 3, 1)

print add_initial_money (30)
