import sys

def rev(a):
	#split sentence into array, then reverse it
	a = a.split()[::-1]

	# join array as a string, strip any space on sides
	a = ' '.join(a).strip()

	return a


def get_input():
	input_array = []

	for line in sys.stdin:
		input_array.append(line)

	return input_array

	
def main():
	string_input = get_input()
	result = ''
	for line in string_input:
		if line.strip():
			result += rev(line) + '\n'

	print(result)

main()