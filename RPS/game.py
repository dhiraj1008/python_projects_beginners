#rock paper scissor game in python ..! 
import random


def play():
    player = input("what's your chose ? 'r' for rock ,'p' for paper and 's' for scissor : ").upper()
    computer = random.choice(['r', 'p', 's']).upper()
    if player == computer:
        return "It\"s a Tie"
    if is_win(player, computer):
        return "You won"
    return "You lost"


def is_win(player, computer):
    if (player == 'R' and computer == 'S') or (player == 'P' and computer == 'R') or (
            player == 'S' and computer == 'P'):
        return True


while 1:
 print(play())
 x= input("for exit:(e) and to contiue:(c)\n")
 if x.lower() == 'e':
    break
 
