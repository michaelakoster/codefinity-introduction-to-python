# Input variables
days_until_expiration = 7  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"


if days_until_expiration <= 3 and stock_level > 50 and product_type == "Perishable":
    print("30% discount applied.")
elif days_until_expiration >= 4 and days_until_expiration <= 6 and stock_level > 50 and product_type == "Perishable":
    print("20% discount applied.")
elif days_until_expiration > 6 and stock_level <= 50 and product_type == "Perishable":
    print("10% discount applied.")
else:
    print("No discount available for non-perishable items.")