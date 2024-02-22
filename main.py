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

# weather = input("What is the weather? rain? sunny? cloudy?")
# if weather == "rain":
#     print("Bring jacket")
# elif weather == "sunny":
#     print("Get your sunglasses out!")
# elif weather == "cloudy":
#     print("Take a hoodie!")
# else:
#     print("just leave the house")

# Grades
# >90 A 
# >80 B 
# >70 C 
# >60 D 
# <60 F 
# grade = int(input("What is your mark?"))
# if grade >= 90:
#     print("A")
# elif grade >= 80 and grade < 90:
#     print("B")
# elif grade >= 70 and grade < 80:
#     print("C")
# elif grade >= 60 and grade < 70:
#     print("D")
# elif grade > 60:
#     print("F")
# else:
#     print("LOL")

 
#Multiple arguments, named arguments
# def greetings( name, greet='hello'):
#     print(f'{greet} {name}')
# greetings('Matt', 'hi')
# greetings(name='Matt', greet='bye')


# String formatting 
# food_amount = float(input("Enter your food amaount: £"))
# tip_percentage = float(input("Enter your tip percentage: "))/100
# tip_amount = food_amount * tip_percentage

# total = food_amount + tip_amount
def billPrice(food_amount, tip_percentage):

    tip_amount = food_amount * tip_percentage
    total = food_amount + tip_amount
    print(total)
    
food_amount = float(input("Enter your food amaount: £"))
tip_percentage = float(input("Enter your tip percentage: "))/100
    
billPrice(food_amount, tip_percentage)