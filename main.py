import random

# For the 1 round only games
def single_play():

# Taking input as in choosing what you gonna play with
    player = input("Please type 'r' for Rock, 'p' for Paper and 's' Scissors: \n").lower()    
    while (player != 'r') and (player != 'p') and (player != 's'):
        player = input("That is not an valid option. Please try again:\n").lower()
    
# Computer choosing randomly
    computer = random.choice(['r', 'p', 's'])

# Will be helpful in printing out the result
    commands = {
        "r" : "Rock",
        "p" : "Paper",
        "s" : "Scissors"
    }
# DRAW
    if player == computer:
        return("It's a draw! Game Over.\n")

# If the output comes true from user_win() then this will trigger, means you won.
    elif user_win(player, computer):
        return(f"You won! The computer used {commands[computer]} against your {commands[player]} and lost.\n")

# Above elif didn't trigger? You lost lol.
    return (f"You lost! The computer used {commands[computer]} against your {commands[player]} and won.\n")


def user_win(player, computer):
# Just so it doesn't get confusing, remeber - r > s, s > p and p > r   ('>' means 'beats')
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

# For the 3 or 5 rounds tournaments. Here everything is same as single_play(), just some minute changes. 
def torni_play():
    player = input("Please type 'r' for Rock, 'p' for Paper and 's' Scissors: \n").lower()
    while (player != 'r') and (player != 'p') and (player != 's'):
        player = input("That is not an valid option. Please try again:\n").lower()
    
    computer = random.choice(['r', 'p', 's'])

    commands = {
        "r" : "Rock",
        "p" : "Paper",
        "s" : "Scissors"
    }

    if player == computer:
        print("It's a draw!.\n")
        # Used for calculating the final score back in Main section
        return("Draw")

    elif user_win(player, computer):
        print(f"You won! Your {commands[player]} beats the computer's {commands[computer]}.\n")
        # Used for calculating the final score back in Main section
        return("Won")

    print(f"You lost! The computer's {commands[computer]} beats your {commands[player]}.\n")
    # Used for calculating the final score back in Main section
    return("Lost")



# -------------MAIN---------------

# Welcome message and Choose what mode to play.
print("\nHello, Player! Welcome to the game of the Mighty Rock-Paper-Scissors!\n\nThere are 2 modes available to play. Single(1 round) and Tournament(Best of 3 or 5 rounds)\n")
game_type = int(input("Type '1' for Single, '2' for Tournament[3 rounds] and '3' for Tournament[5 rounds])\n"))

# Check if the input is valid
while game_type > 3 or game_type < 1:
    game_type = int(input("That is not a valid input, please type a correct one.\n"))

# Single play, here we go!
if game_type == 1:
    print("You chose 1 round only mode!\n")
    print(single_play())
    # Used to exit the whole program so that the '3 or 5 rounds' mode code doesn't get mingled with this one.
    exit()

elif game_type == 2:
    print("You chose 3 rounds tournament mode!\n")
    count, user, comp = 0, 0, 0
    while count < 3:
        # This is used for calculating score.
        outcome = torni_play()
        if outcome == 'Won':
            user += 1
        elif outcome == 'Lost':
            comp += 1
        count += 1

elif game_type == 3:
    print("You chose 5 rounds tournament mode!\n")
    count, user, comp = 0, 0, 0
    while count < 5:
        # This is used for calculating score.
        outcome = torni_play()
        if outcome == 'Won':
            user += 1
        elif outcome == 'Lost':
            comp += 1
        count += 1
else:
    print("If this msg gets printed then there's some error!")

# Final printing section incase player chooses to play 3 or 5 round mode.
if user > comp:
    print(f"You win the tournament.\nFinal Score - You: {user}  |  Computer: {comp}")
elif comp > user:
    print(f"You lost the tournament.\nFinal Score - You: {user}  |  Computer: {comp}")
else:
    print(f"Its a draw.\nFinal Score - You: {user}  |  Computer: {comp}")

