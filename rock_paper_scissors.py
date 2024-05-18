import random

"""
Purpose: to get a player choice from player
Returns: the player choce (int)
"""
def player_input():
  player = int(input("Enter your input:"))
  return player

def machine_input():
  machine = random.randint(0, 2)
  return machine

"""
Purpose: To make decision on the player whether he wins, loses or tie"
Returns:  Tied - when there is a tie
          Won - when player wins
          Lost - when player loses
"""
def decision(player, machine):
  if player == machine:
    return "Tied"

  elif player == 0 and machine ==2:
    return "Won"

  elif player == 1 and machine == 0:
    return "Won"

  else:
    return "Lost"




