import random

bottomofrange = input("What do you want the bottom of the range to be? ")
topofrange = input("What do you want the top of the range to be? ")

random_number = random.randint(int(bottomofrange), int(topofrange))

guess = input("Guess what the random number is. ")

while int(guess) != random_number:
    if int(guess) > random_number:
        print("Too high!")
    else:
        print("Too low!")
    guess = input("Guess what the random number is. ")

if int(guess) == random_number:
    print("You have guessed the number correctly!")