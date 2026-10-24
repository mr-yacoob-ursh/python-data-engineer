
customer_id = int(input("Enter your id : "))
customer_name = input("Enter your name : ")
account_balance = float(input("Enter your balance : "))
is_valid_bal = account_balance > 0

print("===== Customer Data Quality =====")
print(f"Customer ID: {customer_id}")
print(f"Customer Name: {customer_name}")
print(f"Balance: {account_balance}")
print(f"Valid Balance: {bool(is_valid_bal)}")
