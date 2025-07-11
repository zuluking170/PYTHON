
# create a shopping cart programme that will continously ask the user for a food product and the price of the product
# Have an exit clausae if the user wishes to stop adding more things to their cart 
# At the end show the food items and the total cost of the user 

foods = []
prices = []
total = 0 

while True: 
    food = input("Enter a food item to buy or press q to quit: ") 
    if food.lower() == 'q':
        break 
    else: 
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-----Your Cart")  
     
for food in foods:
    print(food, end= " ")

for price in prices: 
    total += price
    
print("\n")    
print(f"Your total is: R{total}")