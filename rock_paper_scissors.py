import random
import sys

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

temp = input("Hi! I'm Rocky, Do you wish to play Rock Paper Scissors with me? ")

while temp == "yes".lower() or temp == "y".lower():
  print("Rock! Paper! Scissors!")
  user_input = input("Make your choice: ").lower()

  if user_input == "rock":
    if computer_choice == "paper":
      print('You win!')
      temp = input("Do you wish to continue? ")
    elif computer_choice == "rock":
      print("It's a tie")
      temp = input("Do you wish to continue? ")
    elif computer_choice == "scissors":
      print("You lose!")
      temp = input("Do you wish to continue? ")

  elif user_input == "paper":
    if computer_choice == "scissors":
      print('You lose!')
      temp = input("Do you wish to continue? ")
    elif computer_choice == "paper":
      print("It's a tie")
      temp = input("Do you wish to continue? ")
    elif computer_choice == "rock":
      print("You win!")
      temp = input("Do you wish to continue? ")

  elif user_input == "scissors":
    if computer_choice == "scissors":
      print("It's a tie")
      temp = input("Do you wish to continue? ")
    elif computer_choice == "paper":
      print("You lose!")
      temp = input("Do you wish to continue? ")
    elif computer_choice == "rock":
      print("You lose!")
      temp = input("Do you wish to continue? ")

  else:
    print("Invalid input! Its rock, paper or scissors")
    
else:
  print("Okay, bye!")
  sys.exit()
