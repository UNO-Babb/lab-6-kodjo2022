#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls[dice1] = rolls[dice1]
    rolls[dice2] = rolls[dice2]
    #find the sum total of the two dice
    total = dice1 + dice2
    rolls[total - 2] = rolls[total - 2] + 1
  
  #print statictics for dice rolls
  for i in range(11):  
    print(str(i + 2) + " : " + str(rolls[i]))
if __name__ == '__main__':
  main()
