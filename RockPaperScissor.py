import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    comp_pick = options[random_number]
    print("computer picked: ", comp_pick + ".")

    
    if user_input == comp_pick:
        print("You both chose " + user_input)
        continue
    
    elif user_input == "rock" and comp_pick == "scissors":
        print("you won")
        user_wins += 1
        

    elif user_input == "paper" and comp_pick == "rock":
        print("you won")
        user_wins += 1
 

    elif user_input == "scissors" and comp_pick == "paper":
        print("you won")
        user_wins += 1
        
    else:
        print("you lost")
        comp_wins += 1

print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
print("Goodbye")