# Mini game - Guess the number
import random

cpu = random.randint(1,100)
counter = 5
while True:
    guess = int(input("Guess the number : "))

    if cpu == guess:
        print("You have guessed the number...")
        break
    elif cpu > guess:
        print("You have guessed smaller number...")
    elif cpu < guess:
        print("You have guessed larger number...")
    counter -= 1
    print("Chances Left :",counter)
    if counter == 0:
        print("You lose...Number was",cpu)
        break
