#Functions go here..
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before.
        response = input(question).lower().strip()
        # If yes, skip the instructions.
        if response == 'yes' or response == 'y':
            response = "yes"
            return response
        # If no, display the instructions.
        elif response == "no" or response == "n":
            response == "no"
            return
        #If other, rerun the code.
        else:
            print("You need to enter yes or no")

#Main routine goes here...
show_instructions = yes_no("Have you played this game before? ")
if show_instructions == "yes":
    print("Skipping Instructions...")
else:
    print("When the game begins, you will be prompted to enter how much money you want to spend to play.\nYou can spend a maximum of $10, and each dollar equals one round.\nEvery round you get to draw a random token. A donkey is worth nothing, a horse or zebra are worth 50 cents and a unicorn is worth $5.\nAfter the round ends, you can spend more of your earnings to play again.Skipping Instructions...")
