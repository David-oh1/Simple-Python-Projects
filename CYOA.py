name = input("What is your name adventurer? ")
print("Welcome,", name, "to this adventure!")



answer = input("You are on a dirt road and it has come to a split. Do you want to go left or right? ").lower()

if answer == "left":
    print("You have come to a jungle. Do you want to: ")
    QL1Answer = input("A) Go through the jungle? or B) go around? :").lower()

    if QL1Answer == "a":
        print("You went into the jungle and died")
    elif QL1Answer == "b":
        print("you walked around for many miles and died")
    else:
        print("Not a valid option. You died.") 


elif answer == "right":
    print("You walked for many miles and came to a river. Do you want to:")
    QR1Answer = input("A) Swim across or B) Cross the bridge? :").lower()

    if QR1Answer == "a":
        print("You tried to swim across but a big titty goth girl distracted you and drowned.")
        print("Also, there's a fucking bridge!!! WHY the hell would you not use it?")

    elif QR1Answer == "b":
        print("You crossed a bridge and on the other side was a guard")
        qr2answer = input("You must pay the tax to continue Do you pay the tax? yes or no :").lower()

        if qr2answer == "yes":
                print("You continue on your journey and meet a stranger")
                print("You make eye contact with them and they have asked you to marry them.")
                qr3answer = input ("Do you say yes or no? :").lower()

                if qr3answer == "yes":
                        print("You person you are marrying turned out to be this really rich dude and he gave you all of his money")
                        print("Congratulations! You win!")

                elif qr3answer == "no":
                        print("The stranger reveavled to you that he was really rich but you won't get any of it so you decided to kill yourself")
                        print("LOL You suck at this game")          
                else:
                        print("Not a valid option, you died")

        elif qr2answer == "no":
            print("You tried to fight the guard but you suck at fighting so you died")

        else:
            print("Not a valid option, you died")

else:
    print("Not a valid option. You died")

print("Thank you for playing", name)