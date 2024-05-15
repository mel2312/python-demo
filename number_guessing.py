import random

def player_input():
  player = input(int("Enter your input between 1 and 3:"))
  return player

def machine_input():
  machine = random.randint(0, 3)
  return machine

def desicion(player, machine):
    if machine == player:
        return "Won"

    else:
        return "Lost"

