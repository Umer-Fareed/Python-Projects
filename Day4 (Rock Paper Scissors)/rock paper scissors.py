#rock paper scissors game
import random
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
rps = [Rock , Paper , Scissors]
#take input from user
print("wellcome to the 'rock', 'paper', 'scissors'")
user_choice = int(input("please choice\n 0: rock 1: paper 2: scissors\n"))
computer_choice = random.randint(0,2)
if user_choice < 0 or user_choice >=3:
    print("You choice an invelid number. You lose: ")

else:
    print(rps[user_choice])
    print("Computer choice: ")
    print(rps[computer_choice])
    if user_choice == computer_choice:
        print("boht choice same game draw")
    elif user_choice > computer_choice:
        print("you win: ")
    elif user_choice == 0 and computer_choice == 2:
        print("you win: ")
    else:
        print(" you lose: ")