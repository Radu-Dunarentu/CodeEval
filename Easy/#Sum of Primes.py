#Sum of Primes
#Write a program which determines the sum of the first 1000 prime numbers. 

def prog():
	result = 0
	prime = 0
	x = 1
	while prime < 1000:
		x += 1
		if is_prime(x):
			prime += 1
			result += x
	return result

def is_prime(x):
	f = False
	for i in range(2,(x/2)+1):
		if x%i == 0:
			f = True
	return not(f)

import sys
sys.stdout.write(str(prog()))