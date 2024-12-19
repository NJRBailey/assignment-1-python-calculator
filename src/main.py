from datetime import datetime

now = datetime.now()
print("It is currently " + str(now.hour) + ":" + str(now.minute) + " on " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + ".")
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
