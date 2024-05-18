#This program will ask the user to enter a number and then ask them to guess a number
import random
print("Greetings! Lets have fun guessing the number!")
print("Enter a positive integer!")
number = input("Enter a number: ")

if number.isdigit():
    if int(number) <= 0:
        print("Enter a positive integer next time!")
    else:
        number = int(number)

else:
    print("Enter a valid integer next time!")

random_number = random.randint(0,number)

print("Let us guess!")
guesses = 0

while True:
    guess_number = input("Your guess: ")

    if guess_number.isdigit():
        if int(guess_number) <= 0:
            print("Enter a positive integer next time!")
            continue
        else:
            guess_number = int(guess_number)

    else:
        print("Enter a valid integer next time!")
        continue

    if guess_number == random_number:
        print("You guessed it right!")
        guesses += 1
        break
    elif guess_number > random_number:
        print("Your guess is higher!")
        guesses += 1
        continue
    else:
        print("Your guess is lower!")
        guesses += 1
        continue

print(f"You took {guesses} amount of guesses to get it right!")