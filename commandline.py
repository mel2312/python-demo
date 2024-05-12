import enum
import random

def input():
  player = input(int("Enter your input:"))
  machine = random.random(0,3)
  return player, machine

