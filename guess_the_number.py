# Mini game - Guess the number
import random

cpu = random.randint(1,100)

while True:
    guess = int(input("Guess the number : "))

    if cpu == guess:
        print("You have guessed the number...")
        break
    elif cpu > guess:
        print("You have guessed smaller number...")
    elif cpu < guess:
        print("You have guessed larger number...")
