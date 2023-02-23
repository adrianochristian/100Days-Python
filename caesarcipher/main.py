#Day 8 -> Function with Input 
#Caeser Cipher
from caesar_art import logo

def caesar(text, shift, function):
    shift_text = ""
    for letter in text:
        if letter in alphabet:
            if function == 'encode':
                shift_text = shift_text + alphabet[int(alphabet.index(letter)) + shift]
            elif function == 'decode':
                shift_text = shift_text + alphabet[int(alphabet.index(letter)) - shift]
        else:
            shift_text = shift_text + letter

    print(f"The {function}d text is {shift_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
    ,'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
    ,'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

print(logo)
function = input("Do you want to encode or decode:\n ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type your shift number: "))

caesar(text, shift, function)

