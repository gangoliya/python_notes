# Step 1: Define an empty dictionary and take values from user
inventory = {} # key- value

num_of_products = int(input("Enter the number of products: "))

print("Enter product details in the order (name, quantity, price): ")

for i in range(num_of_products):
    name = input("Enter the product name: ").strip() # " Apple " strip eliminates the whitespaces
    quantity = int(input(f"Enter the quantity of {name}: ")) # f will define thestring to use variables
    price = float(input(f"Enter the price of {name}: "))
    inventory[name] = {'quantity': quantity, "price" : price}


# inventory[apple] = {"quantity": 3, "price": 1.5}

# Step 2: Make calculation about the total_inventory_value
total_inventory_value = 0
for item in inventory.values(): # values
    total_inventory_value += item["quantity"] * item["price"]
# apple(quantity * price) + cherry(quantity * price) + banana(quantity * price) 
    


print(f"\nTotal Inventory Value: $ {total_inventory_value}") # : .2f float with 2 decimal points




# Step 3: Search for the product in inventory and also put a condition to exit when user types exit and also if product not found!
