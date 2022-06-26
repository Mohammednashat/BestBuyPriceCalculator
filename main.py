# Item price calculator
print("       Welcome to my BestBuy price calculator    ")
tax_rate = 1.13
item_price = input("Item price: \n")
item_price_float = float(item_price)

taxable_or_not = input("Is the item taxable? (y/n) \n")

if taxable_or_not == "y": total_price = item_price_float * tax_rate
print("total price = %.2f" % total_price)

finance_or_not = input("Do you want to finance it thought fairstone? (y/n) \n ")

if finance_or_not == "y": monthly_payment = input("How many months? (6/12) \n")

if monthly_payment == "6":
    total_price=(total_price + 30) / 6
else:
    total_price = (total_price + 70) / 12
payment = str(total_price)
print("Your monthly payment will be $" + payment)
