#fibonacci

import sys

def fibo(n):
	return 0 if n == 0 else 1 if n == 1 else fibo(n-1) + fibo(n-2)


file = open('test.txt')
for line in file:
	print fibo(int(line))

file.close()
