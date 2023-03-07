# Day 2 -> Working with math operators and different data types
# Tip Calculator

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? '))
tip = float(input('What percentage tip would you like to give? '))
people = int(input('How many people would you like to split your bill? '))
result = bill * (1 + (tip / 100)) / people
print(f'Each person should pay: ${round(result, 2)}')
