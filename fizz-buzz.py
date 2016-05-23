import sys

def import_info():
	# converts lines in to array of numbers
	def convert_number(line):
		str_array = line.split(' ')
		num_array = []
		for x in str_array:
			num_array.append(int(x))
		
		return num_array

	# import file using python-file.py < file-to-read.txt from console 
	file = sys.stdin
	# to hold all lines
	file_array = []
	# iterate over every line and convert into array with ints
	for line in file.readlines(): 
		# run each line thru convert_number function to get an array
		# that way you can manipulate it in another function
		file_array.append(convert_number(line))

	# return one big array with sub arrays
	return file_array

def fizz_buzz(data):
	def fizz_buzz_testing(subarray):
		# x is first divisor, y second divisor, n is max range
		x = subarray[0]
		y = subarray[1]
		n = subarray[2]

		output_string = ''
		
		# fizz buzz testing
		for i in range(1,n+1):
			if i % x == 0 and i % y == 0:
				output_string += 'FB '
			elif i % x == 0:
				output_string += 'F ' 
			elif i % y == 0:
				output_string += 'B '
			else: 
				output_string += str(i) + ' '

		return output_string

	# answer string to return and output
	answer_string = ''

	# iterate over all subarrays and apply testing, then add to answer_string
	for subarray in data:
		answer_string += '\n' + fizz_buzz_testing(subarray)

	return answer_string

def main():
	data = import_info()
	answer = fizz_buzz(data)
	print(answer)

main()