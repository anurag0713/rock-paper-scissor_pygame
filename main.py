# This is a rough version, will be making some changes in the wording to make it seem more real and less confusing to play
import random

def play():
    user = input("Choose 'r' for rock, 'p' for paper and 's' scissors: \n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return("It's a tie!")

    elif user_win(user, computer):
        return(f"You won! The computer used {computer} against your {user} and lost.")

    return (f"You lost! The computer used {computer} against your {user} and won.")

def user_win(player1, comp):
    
    # r > s, s > p and p > r
    if (player1 == 'r' and comp == 's') or (player1 == 's' and comp == 'p') or (player1 == 'p' and comp == 'r'):
        return True
    
print(play())
