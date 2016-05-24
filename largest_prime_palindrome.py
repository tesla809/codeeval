# Write a program which determines the largest prime palindrome less than 1000.
# Should print 929 

import math 
n = 1000

# work backwards
# find palindrome
# test if prime

def prime_palindrome_check(n):
	def is_prime(n):
	    if n==2 or n==3: return True
	    if n%2==0 or n<2: return False
	    for i in range(3,int(n**0.5)+1,2):# only odd numbers
	        if n%i==0:
	            return False    
	    return True

	for i in range(n, 0,-1):
		if str(i) == str(i)[::-1]:
			if is_prime(i) == True:
				return str(i)
	
def main():
	print(prime_palindrome_check(n))
	
main()