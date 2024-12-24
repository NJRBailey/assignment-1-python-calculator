import re

def is_valid_calculation(user_input, require_first_number=False):
	if require_first_number == True:
		pattern = r"(\-?\d+\.?\d*)\s+[\+\-\/\*\^x]\s+(\-?\d+\.?\d*)"
		return bool(re.match(pattern, user_input))
	else:
		pattern = r"(\-?\d+\.?\d*)?\s*[\+\-\/\*\^x]\s+(\-?\d+\.?\d*)"
		return bool(re.match(pattern, user_input))

def parsed_input(data={}):
	default = {
		"numbers": [],
		"operator": None,
		"clear": False,
		"end": False,
		"help": False,
	}
	return default | data
def user_input(previous_result=None):
	user_data = input("Enter a calculation: ")
	if user_data == "help" or user_data == "h": return parsed_input({"help": True})
	elif user_data == "c": return parsed_input({"clear": True})
	elif user_data == "end": return parsed_input({"end": True})
	else:
		if is_valid_calculation(user_data, require_first_number=previous_result == None):
			numbers = re.findall(r"\-?\d+\.?\d*", user_data)
			operator = re.findall(r"[\+\-\/\*\^x]\s", user_data)[0].strip()
			return parsed_input({"numbers": list(map(float, numbers)), "operator": operator})
		else:
			return parsed_input()