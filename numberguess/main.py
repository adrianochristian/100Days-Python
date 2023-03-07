# Day 12 -> Namespaces and Scope
# Number Guessing
import random


def game():
    number = random.randint(0, 100)
    print("Welcome to the Number Guessing Game\nI'm thinking of a number between 0 and 100")
    difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You won!")
            return
        if guess > number:
            print("Too High")
        if guess < number:
            print("Too Low!")
        lives -= 1
        print(f"You have {lives} attemps left.")


game()
