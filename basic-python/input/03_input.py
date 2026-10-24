product_name = input("Enter your product name : ")
quantity = int(input("How much quantity : "))
price = float(input("How much price : "))
total_price = quantity * price

print("===== Sales Record =====")
print(f"Product : {product_name}")
print(f"Quantity : {quantity}")
print(f"Price : {price}")
print(f"Total price : {total_price}")

print("==== Variable data types ====")
print(type(product_name))
print(type(quantity))
print(type(price))
print(type(total_price))