#Day 5 -> For Loops, range and code blocks 
#Password Generator
import random

print("Welcome to the Pyssword Generator!")

#Lists
letter_list = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z']
number_list = ['1','2','3','4','5','6','7','8','9','0']
symbol_list = ['!', '<', '>', '#','/', '^','%', '&', '*']

#App
letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))
password = [];

for char in range(1, letters):
    password.append(random.choice(letter_list))

for char in range(1, symbols):
    password.append(random.choice(symbol_list))

for char in range(1, numbers):
    password.append(random.choice(number_list))

random.shuffle(password)
print(password)
result = ""

for char in password:
    result += char

print(f"Here is your password: {result}")
