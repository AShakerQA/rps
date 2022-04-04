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

#sanitize user input for 0,1 or 2
while True:
    user_choice = input("Fancy a game of Rock, Paper, Scissors? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if user_choice not in ("0", "1", "2"):
        print("You must enter either: 0, 1 or 2")
    else:
        break
print(game_images[int(user_choice)])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

int_user_choice = int(user_choice)

if int_user_choice >= 3 or int_user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif int_user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and int_user_choice == 2:
  print("You lose")
elif computer_choice > int_user_choice:
  print("You lose")
elif int_user_choice > computer_choice:
  print("You win!")
elif computer_choice == int_user_choice:
  print("It's a draw")
