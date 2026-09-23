name = input("What's your name? ")

print(f"Welcome, {name}!")
age = int(input("How old are you? "))

print("Next year you will be", age + 1)

age = int(input("How old are you? "))

if age >= 15:
    print("You are an adult.")
else:
    print("You are under 15.")

for number in range(1, 20):
    print(number)

for i in range(5):
    print("I am learning to code!")


def greet(Antman):
    print("Hello, " + Antman + "!")

greet("Antman")