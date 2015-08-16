#Prime Palindrome
#Write a program which determines the largest prime palindrome less than 1000. 

def my_range(start, end, step):
    while start >= end:
        yield start
        start -= step
def is_palindrome(data):
		w = str(data)
		m = len(w)
		for i in range(0,m):
			if w[i] != w[m-i-1]:
				return False
		return True

def prog():
	for x in my_range(1000, 2, 1):
		f = False
		for i in range(2,500):
			if x%i == 0:
				f = True
		if not(f) and is_palindrome(x):
			return x
		f = False;

import sys
sys.stdout.write(str(prog()))