from enum import Enum
import rock_paper_scissors as rpk
import number_guessing as ng

class rock_paper_scissors(Enum):
    rock = 0
    paper = 1
    scissors = 2

play = True
while play:
    print("Welcome to arcade world")
    player = int(input("Which game would you like to"))
    play_again = "y"
    while((player == 1 or player == 2) and play_again == "y"):
        if(player == 1):
            print("Rock")
            player_input = rpk.player_input()
            machine_input = rpk.machine_input()
            play_again = input("Do you want to play again? y or n")


        else:
            print("Paper")
            ng.game_input()
            ng.machine_input()
            play_again = input("Do you want to play again? y or n")

