# List of drinks available
drinks = ["Coca-Cola", "Coffee", "100 Plus", "Sprite"]
# Drink number and Prices 1: Coca-Cola = $1 , 2: Coffee = $2 , 3: 100 Plus = $3  , 4: Sprite = $4
drink_prices = {1:1, 2:2, 3:3, 4:4}
# User to input the drink number
num = int(input("Insert drink number: "))
# Check if the selected drink number is valid
if num in drink_prices:
    # Payment based on the drink price.
    payment = int(input("Please insert the corresponding note for the drink: "))
    price = drink_prices[num]
    if payment < price:
        print("Insufficient funds. Please insert exactly the amount required.")
    elif payment == price:
        print("Here's your drink:", drinks[num - 1])
    else:
        print( "Here's your drink:", drinks[num - 1],",", "Balance = RM", payment - price)
else:
    print("Invalid selection")
