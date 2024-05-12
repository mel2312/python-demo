import enum
import random

"""
Purpose: to get a player choice from player
Returns: the player choce (int)
"""
def player_input():
  player = input(int("Enter your input:"))
  return player

def machine_input():
  machine = random.randint(0, 2)
  return machine

def decision(player, machine):



