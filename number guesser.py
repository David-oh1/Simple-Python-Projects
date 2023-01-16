import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("please type a number larger than 0.")
        quit()
else:
    print("Please type in a number.")
    quit()

r = random.randrange(top_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number")
        continue

    if user_guess == r:
        print("you got it")
        break
    
    elif user_guess > r:
        print("you were above the number")

    else:
        print("You were below the number")

print("you got it in", guesses, "guesses")


