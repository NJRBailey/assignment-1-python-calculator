first_number = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
second_number = float(input("Enter the second number: "))
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
