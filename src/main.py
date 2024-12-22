from startup import clock_message, random_message
from calculate import calculate

print(clock_message())
print(random_message())

run = True
result = None
while run == True:
	result = calculate(result)
	print(result)
	restart_input = input("Press enter to perform another calculation, or type 'end' to finish: ")
	if restart_input == "end":
		run = False
