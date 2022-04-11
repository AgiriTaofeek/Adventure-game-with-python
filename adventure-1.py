# Import time module to the print interval time delay
import time

# Import random module to help make choices at random from a list
import random


# function to print all messages within a spaced time interval
def print_pause(msg):
    print(msg)
    time.sleep(2)


# function that runs whole game and stores the piece and option variable
def run_game():
    piece = []
    option = random.choice(["witch", "monster", "bush-baby", "unicorn", "el"])
    intro(piece, option)
    choices(piece, option)


# function that calls the print_pause function and print the intro messages
def intro(piece, option):
    print_pause("You are on a mission to save the princess in a forbidden "
                "jungle,\n")
    print_pause(
        "It is known that anyone that goes there never returns because of a "
        + option
        + ".\n"
    )
    print_pause("Westwards is a red door.\n")
    print_pause("Eastwards is a green door.\n")
    print_pause("In your hand is a magic wand.\n")


# function for choices made between 1 and 2
def choices(piece, option):
    print_pause("Enter 1 to go through the red door.")
    print_pause("Enter 2 to go through the green door.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2)\n")
        if choice1 == "1":
            # red_door function call
            red_door(piece, option)
            break
        elif choice1 == "2":
            # green_door function call
            green_door(piece, option)
            break
        elif choice1 != "1" or choice1 != "2":
            print_pause("Do try to Enter 1 or 2 😔")


# function to fight or run
def fight_or_run(piece, option):
    if "hunter-gun" in piece:
        print_pause(
            "\nBefore " + option + " could attack,  you shot it with the"
            " hunter-gun"
        )
        print_pause("\nAfter that shot,  the " + option + " fled.")
        print_pause("\nYou saved the princess😍.\n")
    else:
        print_pause("\nYou ran away without saving the princess")
        print_pause("\nWithout the hunter-gun, nothing can be done")
        print_pause("\nYou are defeated by " + option + ".\n")


# function for going through red door
def red_door(piece, option):
    if "hunter-gun" in piece:
        print_pause("\nWalk through the red door")
        print_pause("\nYou don't have to scared")
        print_pause("\nA hunter-gun should keep you safe")
    else:
        print_pause("\nWalk through the red door")
        print_pause("\nTry not to make any noise")
        print_pause("\nA hunter-gun will appear if don't make any sound")
        print_pause("\nPick your hunter-gun, better than magic wand.")
        print_pause("\nWalk back outside silently.\n")
        piece.append("hunter-gun")
    choices(piece, option)


# function for going through green door
def green_door(piece, option):
    print_pause("\nWalk through the green door")
    print_pause("\nYou are about to get in when you heard a noise from inside")
    print_pause("\n'This is the " + option + "!!!!'")
    print_pause("\n'Are you here to save the princess?'")
    print_pause("\n'You have to fight me to do that'\n")
    if "hunter-game" not in piece:
        print_pause("I have to run from this place😥 without my hunter-gun\n")

    while True:
        choice3 = input("Would you like to (1) fight or (2) run away?")
        if choice3 == "1":
            fight_or_run(piece, option)
            # function call to restart game
            restart_game()
            break
        elif choice3 == 2:
            print_pause("\nYou ran out unhurt without saving the princess.\n")
            # function call to choices
            choices(piece, option)
            break


def restart_game():
    restart = input("Would you like to play again? (Y/N)").lower()
    if restart == "y":
        print_pause("\n\n\nExcellent! Restarting the game ... \n\n\n")
        # function call of run_game
        run_game()
    elif restart == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        restart_game()


# function call to run the whole game
if __name__ == "__main__":
    run_game()
