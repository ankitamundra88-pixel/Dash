actual_cost = float(input("Please Enter the actual Product Price: "))
sale_amount = float(input("Please Enter the Sale Amount: "))

if (sale_amount > actual_cost):
    amount_saved = sale_amount - actual_cost
    print ("Total profit = {0}". format(amount_saved))
else:
    print("No Profit!!!")