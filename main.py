# your_name = input("please enter your name: ")
# print("Hi", your_name) 

# String formatting 
# food_amount = float(input("Enter your food amaount: £"))
# tip_percentage = float(input("Enter your tip percentage: "))/100
# tip_amount = food_amount * tip_percentage

# total = food_amount + tip_amount
# print("---------------------")
# print(f'Food Amount: £{food_amount}')
# print(f'Tip Amount: £{tip_amount}')
# print(f'Total Bill: £{total}')
# print("---------------------")

# Boolean

weather = input("What is the weather? rain? sunny? cloudy?")
if weather == "rain":
    print("Bring jacket")
elif weather == "sunny":
    print("Get your sunglasses out!")
elif weather == "cloudy":
    print("Take a hoodie!")
else:
    print("just leave the house")