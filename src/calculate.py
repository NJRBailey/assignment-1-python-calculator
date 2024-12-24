def calculate(first_number, operator, second_number):
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
