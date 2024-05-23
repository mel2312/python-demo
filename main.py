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
    print("these are the options:\n 1)Rock Paper Scissors\n 2)Number Guessing")
    player = int(input("Which game would you like to play?"))
    play_again = "y"
    while (player == 1 or player == 2) and play_again == "y":
        if player == 1:
            print("Lets play Rock Paper Scissors!")
            print("what do you choose? rock = 0, paper = 1 or scissors = 2: ")
            player_input = rpk.player_input()
            machine_input = rpk.machine_input()
            result = rpk.decision(player_input, machine_input)
            print(f"Computer chose {str(rock_paper_scissors(machine_input)).replace("rock_paper_scissors.", '')} and you chose {str(rock_paper_scissors(player_input)).replace("rock_paper_scissors.", '')}")

            if result == "Tied":
                print("You tied")

            elif result == "Won":
                print("Player won")

            else:
                print("Computer won")

            play_again = input("Do you want to play again? y or n: ")


        else:
            print("Paper")
            ng.game_input()
            ng.machine_input()
            play_again = input("Do you want to play again? y or n")

    print("Thanks for playing!")
    print("Do you want to play again in the arcade? y or n")