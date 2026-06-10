number = input("Enter a number: ")
try: square_root = float(number) ** 0.5
except ValueError: print("Invalid input. Please enter a valid number.")
else: print("The square root of", number, "is", square_root)
