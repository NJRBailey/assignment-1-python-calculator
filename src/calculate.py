def calculate(previous_result=None):
	first_number = None
	while first_number == None:
		try:
			if previous_result == None:
				first_number = float(input("Enter the first number: "))
			else:
				first_number_input = input("Enter the first number, or press enter to use previous result: ")
				if first_number_input == "":
					first_number = previous_result
				else:
					first_number = float(first_number_input)
		except ValueError:
			print("Invalid input. Please enter a number.")
	operator = None
	while operator == None:
		user_input = input("Enter the operator: ")
		if user_input in ["+", "-", "*", "x", "/", "^"]:
			operator = user_input
		else:
			print("Invalid input. Please enter a valid operator (+ - * x / ^).")
	second_number = None
	while second_number == None:
		try:
			second_number = float(input("Enter the second number: "))
		except ValueError:
			print("Invalid input. Please enter a number.")
	if operator == "+":
		return first_number + second_number
	elif operator == "-":
		return first_number - second_number
	elif operator == "*" or operator == "x":
		return first_number * second_number
	elif operator == "/":
		return first_number / second_number
	elif operator == "^":
		return first_number ** second_number
