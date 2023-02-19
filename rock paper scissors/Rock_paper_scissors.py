import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose, Press 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice >= 3 or user_choice <0 :
    print("you chose an invalid number, YOU LOSE!")
else:
    print (game_images[user_choice])  

    computer_choice = random.randint(0,2)
    print("computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print ("YOU WIN!")
    elif computer_choice == 0 and user_choice == 2:
        print ("YOU LOSE!")
    elif computer_choice > user_choice:
        print ("YOU LOSE!")
    elif user_choice > computer_choice:
        print ("YOU WIN!")
    elif computer_choice == user_choice:
        print ("IT'S A DRAW!")

