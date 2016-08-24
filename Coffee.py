coffee_price = 10.5
shipping = 0.86
fee = 1.5

total_price = 0

order_size = float(input("How many lbs of coffee do you want? "))

total_price = (coffee_price * order_size) + (shipping * order_size) + fee

print("Total order amount is: $" + str(total_price))
