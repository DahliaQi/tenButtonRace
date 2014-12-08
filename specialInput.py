#! /usr/bin/env python

def int_input(prompt):
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			return answer
		except ValueError:
			int_input("That isn't a number dude. please try again.")
			

def name_input(name):
	name = raw_input("What's your name please?")
	if len(name) > 10:
		name = name[0:10]
		print("That's too long, let me give you a cuuuuute nickname {}.".format(name))
	return name
			
def float_input(prompt):
		number = raw_input(prompt)
		try:
			number = float(number)
			return number
		except ValueError:
			float_input("This is not a float, please try again.")