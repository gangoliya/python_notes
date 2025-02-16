# Inventory Management System

# Step 1: Get the product details from user
inventory = {}  # empty list

num_of_products = int(input("Enter number of products: "))

print("Enter product details (name, quantity, price): ")

for i in range(num_of_products):
    name = input("Enter Product Name: ").strip()
    quantity = int(input(f"Enter quantity of {name}: "))
    price = float(input(f"Enter price of {name}: "))
    inventory[name] = {"quantity": quantity, "price": price} 

# Step 2: Calculate total inventory value
total_value = 0
for item in inventory.values():  # values() function
    total_value += item["quantity"] * item["price"] # Add each product's total cost
print(f"\nTotal inventory value: ${total_value: .2f}")


# Step 3: Search functionality with loop
while True:
    search_text = input("\nSearch for a product (or type 'exit' to stop): ").strip()

    if search_text.lower() == "exit":
        break

    if search_text in inventory:
        item = inventory[search_text]
        print(f"Product: {search_text}, Quantity: {item['quantity']}, Price: ${item['price']: .2f}")
        if item["quantity"] < 5:
            print("Warning: Low Stock!")
    else:
        print("Product not found!")