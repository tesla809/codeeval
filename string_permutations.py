# Write a program which prints all the permutations of a string in alphabetical order.
# We consider that digits < upper case letters < lower case letters. 
# The sorting should be performed in ascending order.

import sys
from itertools import permutations


def get_input():
	input_array = []

	for line in sys.stdin:
		input_array.append(line)

	return input_array

def permutation(string):
	# uses the permutations function from the itertools module 
	permutations_list = [''.join(p) for p in permutations(string.rstrip('\n'))]
	
	# reverse the order keep in ascending order with digits < upper cast < lower case
	permutations_list = set(permutations_list[::-1])
	
	# test for length len(permutations_list)
	# turns list into string 
	return ','.join(permutations_list)

def main():
	test = get_input()
	for word in test:
		print(permutation(word))

main()
