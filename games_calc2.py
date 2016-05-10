#set all entities

# Set money
initial_money = 0
target_money = 0
def set_money (initial, target):
    initial_money = initial
    target_money = target

# Add ingredient
ingr = {}
def add_ingr (name, plant_price, qty):
    ingr[name] = plant_price, qty

# Add product
products = {}
def add_product (ingr, price):
    return 0

#calculate prodcuts qty
#def calculate_products_qty (#target money, #init_money, #product sell price)

#calculate ingr qty


add_ingr ('tomato', 1, 3)
add_ingr ('pepper', 2, 3)
print ingr

set_money (5000, 50000)

print initial_money
print target_money
