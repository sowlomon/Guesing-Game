import time


name = input("what is your name: ")


print()
print("WELCOME " + name.upper() + " TO MY GUESS GAME!.....")


time.sleep(5)

print()
print("TYPE IN THE WORD YOU CHOOSE!")

guess_word = "FOOD"


begin_guess = 1


guess_limit = 5


while begin_guess < guess_limit:
    whats_ur_guess = input("Enter your guess: ")
    begin_guess += 1
    if whats_ur_guess == guess_word.upper():
        print()
        print("Congratutions! " + name.title() + "\nyou are correct!")
        break
    else:
        print()
        print("You are wrong " + name.title() +  ":("  "\ntry again! ")


