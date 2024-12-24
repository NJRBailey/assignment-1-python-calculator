from datetime import datetime
from random import randint

def clock_message():
	now = datetime.now()
	return "It is currently " + str(now.hour) + ":" + str(now.minute) + " on " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + "."

def random_message():
	messages = [
	'"If I cannot do great things, I can do small things in a great way." —Martin Luther King, Jr.',
	'"Act as if what you do makes a difference. It does." —William James',
	'"Be the change that you wish to see in the world." —Mahatma Ghandi',
	'"Don\'t sit down and wait for the opportunities to come. Get up and make them." —Madam C.J. Walker',
	'"Opportunity is missed by most people because it is dressed in overalls and looks like work." —Thomas Edison'
	]
	message_index = randint(0, len(messages) - 1)
	return(messages[message_index])

def help_message():
	return(
		"""
		Enter a calculation with two numbers and an operator separated by spaces.
		If you have already done a calculation, you can use the previous result by entering an operator and a number.
		Operators: + - * / ^
		To clear the previous result, enter 'c'.
		To end the program, enter 'end'.
		To see this message again, enter 'help'.
		"""
	)