# Author: Anton Tkacz
# Last updated: 16:45, 29 March 2014
# Password generator
# Usage: The user can enter a value for the length of the password 
# with a minimum of 6, alternatively the length defaults to 8

import sys
from random import randint

def main():
	try:
		length = int(sys.argv[1])
	except:
		length = 8

	if length < 6:
		sys.exit("Usage: python password.py [n]\n\
n is by default 8, and not less than 6")

	print password(length)

def password(length):
	# Suitable symbols for password, edit at will
	symbols = "!@#$%^&*_="

	# pword_elem is a list of the amount of character elements of each
	# kind being contained within this passord
	# 0 - uppercase alphabetic characters
	# 1 - lowercase alphabetic characters
	# 2 - symbols
	# 3 - numeric characters
	# It would ideally be a dictionary, however as it is easiest to pop an
	# integer randomly from a list, a list is a better implementation
	pword_elem = []
	pword = []

	# Calculate number of password elements
	num_alpha = length/2
	pword_elem += randint(1, num_alpha) * [0]
	pword_elem += (num_alpha - pword_elem.count(0)) * [1]
	pword_elem += (length - num_alpha)/3 * [2]
	pword_elem += (length - num_alpha - pword_elem.count(2)) * [3]

	while length > 0:
		# Define char_type as a type of character randomly from the list of
		# password elements and then append it to the password list
		char_type = pword_elem.pop(randint(0, length - 1))

		if char_type == 0:
			pword.append(chr(randint(65,90)))
		elif char_type == 1:
			pword.append(chr(randint(97, 122)))
		elif char_type == 2:
			pword.append(symbols[randint(0,9)])
		else:
			pword.append(str(randint(0, 9)))
		
		length -= 1

	password = "".join(pword)
	return password

main()