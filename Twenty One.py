import time
import os
import random
def clear():
  os.system("cls" if os.name=="nt" else "clear")

user=[]
computer=[]
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
draw="""
 _______        _______ _   _ _______   __        ___  _   _ _____ 
|_   _\ \      / / ____| \ | |_   _\ \ / /       / _ \| \ | | ____|
  | |  \ \ /\ / /|  _| |  \| | | |  \ V /       | | | |  \| |  _|  
  | |   \ V  V / | |___| |\  | | |   | |        | |_| | |\  | |___ 
  |_|    \_/\_/  |_____|_| \_| |_|   |_|         \___/|_| \_|_____|
"""

def random_card(man,time):
  for cards in range(time):
    a=random.choice(card)
    man.append(a)

def sure(man):
  if 11 in man and sum(man) >20:
    man.remove(11)
    man.append(1)

  
def game():
  print("""Choose a game to start........
1- Froggy
2-Twenty one
3-Snake
______________""")
  if (input(" ").lower())!='twenty one':
    print("Invaild choice")
    game()

  clear()
  time.sleep(3)
  print("starting game")
  print(draw)
  random_card(user,2)    
  random_card(computer,2)

  while True:
    time.sleep(2)
    print(f"Your cards are {user} current score is {sum(user)}")
    print(f"\ncomputer’s first card is {computer[1]}")
    time.sleep(2)
    
    if sum(user)>=21:
      break
    sure(user)
    
    if (input("\nGet another card? y/n ").lower())=='y' :
      random_card(user,1)
      continue
    else:
      break
  sure(computer)
  sure(user)
  while sum(computer)<17:
    random_card(computer,1)
  print(f"\nYour final hand :{user} with score {sum(user)} ")
  print(f"\ncomputer’s final hand: {computer} with score {sum(computer)}")
 
      
  if sum(user)>21 and sum(computer)<21:
      print("You lose\n")
  elif sum(computer) >21 and sum(user) <21:
      print("computer went over 21, You win\n")
  elif sum(user)==sum(computer):
      print("Draw\n")
  elif sum(user) <21 and sum(computer)<21 and sum(user)>sum(computer):
      print("You win\n")
  elif sum(user) <21 and sum(computer)<=21 and sum(user)<sum(computer):
      print("You lose\n")
  else:
      print("You win\n")

  

    
game()
