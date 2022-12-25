import random

max_guesses = 3
number_of_guesses = 0
lost = True

chances_left = max_guesses - number_of_guesses

my_number = random.randint(0, 100)

name = input('Enter your name: ')
greeting_message = print("Hello " + name + ". You have a total of {} chances, this is your first one. Enjoy!".format( str(max_guesses)))

while number_of_guesses < max_guesses:
  number_of_guesses += 1
  chances_left -= 1

  try:
    user_input = input("guess a number: ")

  except ValueError:
    print("That is not a valid integer, you loose a chance!")
  finally:
    print("Chances left: " + str(chances_left))
    
  if int(user_input) < my_number:
    print("Well the number was too low")
  elif int(user_input) > my_number:
    print("Well that number is too high")
  else:
    print("Good job! you got it in {} guesses".format(number_of_guesses))
    lost = False
    break
if lost:
  print("You lost! The number I was thinking about is {}".format(my_number))
