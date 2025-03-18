import random

# Define choices
rock = 0
paper = 1
scissors = 2

# Get user input
user_choice = int(input('Type 0 for rock, 1 for paper, or 2 for scissors: '))

# Ensure input is valid
if user_choice not in [rock, paper, scissors]:
    print("Invalid choice! Please select 0, 1, or 2.")
else:
    # Computer makes a random choice
    choices = [rock, paper, scissors]
    computers_choice = random.choice(choices)

    # Print user and computer choices
    print(f'You chose {user_choice}, computer chose {computers_choice}')

    # Game logic
    if user_choice == computers_choice:
        print("It's a draw!")
    elif (user_choice == rock and computers_choice == scissors) or \
         (user_choice == paper and computers_choice == rock) or \
         (user_choice == scissors and computers_choice == paper):
        print("You won!")
    else:
        print("You lost!")




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
print()
