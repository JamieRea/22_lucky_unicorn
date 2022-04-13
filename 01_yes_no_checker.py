#This function checks if a user has played the game before.
def yes_no():
    skip = input("Have you played this game before?").lower().strip()
    if skip == 'yes' or skip == 'y':
        print("Skipping Instructions...")
    elif skip == 'no' or skip == 'n':
        #Displays the instructions for the user.
        print("When the game begins, you will be prompted to enter how much money you want to spend to play.\nYou can spend a maximum of $10, and each dollar equals one round.\nEvery round you get to draw a random token. A donkey is worth nothing, a horse or zebra are worth 50 cents and a unicorn is worth $5.\nAfter the round ends, you can spend more of your earnings to play again.")
    else:
        #Lets the user know they need to enter Yes or No if there is an error.
        print("You need to enter Yes or No.")
        yes_no()
introduction = input("Welcome to Lucky Unicorn! Press any key to begin!")
yes_no()


