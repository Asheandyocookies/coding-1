def multiply_by_three():
    for w in range(1, 16):
        print(w * 3)

multiply_by_three()


#5 numbers. once it has reached 5 numbers your function should print out the number list and stop and use the list method



def collect_five_numbers():
    number_list = []
    
    while len(number_list) < 5:
        user_input = float(input("Enter a number: "))
        number_list.append(user_input)
        
    print("Your list:", number_list)

    
