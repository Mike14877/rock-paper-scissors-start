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

image = [rock, paper, scissors]

user_choose = int(input("What do you wany choose ?\n Typing 0 for Rock\n Typing 1 for Paper\n Typing 2 for Scissors\n"))

computer_choose = random.randint(0,2)

print(f"The computer choose {computer_choose}  ")

if computer_choose == 0:
  print(image[computer_choose])
elif computer_choose == 1:
  print(image[computer_choose])
else : 
  print(image[computer_choose])


print(f"The user choose {user_choose}  ")

if user_choose == 0:
  print(image[user_choose])
elif user_choose == 1:
  print(image[user_choose])
else : 
  print(image[user_choose])

if user_choose == 0 and computer_choose == 2:
  print("You Won !")
elif computer_choose == 0 and user_choose == 2:
  print("You Lose !")
elif user_choose > computer_choose :
  print("You Won !")
elif computer_choose > user_choose:
  print("You Lose !")  
elif computer_choose == user_choose:
  print("Draw, Try Again")