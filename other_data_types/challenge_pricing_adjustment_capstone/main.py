# Create the Dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# --- Check and Update Price of Eggs ---
category, price, stock = grocery_inventory["Eggs"]

if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    price -= 1
    grocery_inventory["Eggs"] = (category, price, stock)
else:
    print("The price of Eggs is reasonable.")

# --- Add a New Item: Tomatoes ---
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

# --- Manage Stock for Milk ---
category, price, stock = grocery_inventory["Milk"]

if stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    stock += 20
    grocery_inventory["Milk"] = (category, price, stock)
else:
    print("Milk has sufficient stock.")

# --- Remove Apples if Price Exceeds 2 ---
category, price, stock = grocery_inventory["Apples"]

if price > 2:
    del grocery_inventory["Apples"]
    print("Apples removed from inventory due to high price.")

# --- Final Print ---
print(f"Updated inventory: {grocery_inventory}")
