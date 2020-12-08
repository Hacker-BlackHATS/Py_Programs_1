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

options = [rock, paper, scissors]

user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[user_chose])

computer_chose = random.randint(0,2)
print(f"\nComputer chose ::\n{options[computer_chose]}")

user_win_pair = [(0, 2), (1, 0), (2, 1)]

if (user_chose, computer_chose) in user_win_pair:
    print("You win!")
elif user_chose == computer_chose:
    print("It's a draw...")
else:
    print("You lose!!!")
