seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

overstock_risk = (seasonal == True) and (current_stock > high_stock_threshold)
discount_eligible = not(selling_well == True) and not(on_sale == True)
make_discount = (overstock_risk == True) or (discount_eligible == True)


print("Should the item be discounted?", make_discount)