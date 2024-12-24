from messages import clock_message, random_message, help_message
from input import user_input
from calculate import calculate

print(clock_message())
print(random_message())
print(help_message())

run = True
result = None
while run == True:
	user_command = user_input(previous_result=result)
	if user_command["help"] == True:
		print(help_message())
		continue
	elif user_command["clear"] == True:
		result = None
		print("Cleared.")
		continue
	elif user_command["end"] == True:
		run = False
		continue
	elif user_command["numbers"] == [] or user_command["operator"] == None:
		print("Invalid input, please try again.")
		continue
	else:
		if len(user_command["numbers"]) == 1:
			result = calculate(result, user_command["operator"], user_command["numbers"][0])
		else:
			result = calculate(user_command["numbers"][0], user_command["operator"], user_command["numbers"][1])
	print(result)
