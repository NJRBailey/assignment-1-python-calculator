from datetime import datetime
from random import randint

now = datetime.now()
print("It is currently " + str(now.hour) + ":" + str(now.minute) + " on " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + ".")

messages = [
  '"If I cannot do great things, I can do small things in a great way." —Martin Luther King, Jr.',
  '"Act as if what you do makes a difference. It does." —William James',
  '"Be the change that you wish to see in the world." —Mahatma Ghandi',
  '"Don\'t sit down and wait for the opportunities to come. Get up and make them." —Madam C.J. Walker',
  '"Opportunity is missed by most people because it is dressed in overalls and looks like work." —Thomas Edison'
]
message_index = randint(0, len(messages) - 1)
print(messages[message_index])

first_number = None
while first_number == None:
  try:
    first_number = float(input("Enter the first number: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
operator = None
while operator == None:
  user_input = input("Enter the operator: ")
  if user_input in ["+", "-", "*", "/", "^", ]:
    operator = user_input
  else:
    print("Invalid input. Please enter a valid operator (+ - * / ^).")
second_number = None
while second_number == None:
  try:
    second_number = float(input("Enter the second number: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
if operator == "+":
  print(first_number + second_number)
elif operator == "-":
  print(first_number - second_number)
elif operator == "*":
  print(first_number * second_number)
elif operator == "/":
  print(first_number / second_number)
elif operator == "^":
  print(first_number ** second_number)
