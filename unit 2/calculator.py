

#step 2: the numbers should be typed in by a user



# phase 1: function Definition- actual code
from random import choice


def calculate_add():
    print("Program has started: please type 2 numbers to add:")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)


def calculate_subtract():
    print("Please type 2 numbers to subtract:")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)


def calculate_multiply():
    print("Please type 2 numbers to multiply:")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)


def calculate_divide():
    print("Please type 2 numbers to divide:")
num1 = int(input())
num2 = int(input())
print(num1 / num2)
    
if choice == '1':
    calculate_add()
elif choice == '2':
    calculate_subtract()
elif choice == '3':
    calculate_multiply()
elif choice == '4':
    calculate_divide()

else:
    print("error: something went wrong with your choice")




def get_ticket_price(age): 
    if age <7:
        print("your ticket is 8.00")
    elif age >= 8 and age <=20:
        print('your ticket is 12.00')
    elif age >=21 and age <=60:
        print('your ticket is 20.00')
    elif age >=61:
        print("your ticket is free")
    else:
        print("Dumb asf follow the rules")

movieTicket()