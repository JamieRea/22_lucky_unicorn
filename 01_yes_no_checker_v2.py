#Functions go here...
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
# Main routine goes here...
show_instructions = yes_no("Have you played this game before? ")
print("You chose {}".format(show_instructions))


