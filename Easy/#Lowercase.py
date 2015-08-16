#Lowercase
#Given a string write a program to convert it into lowercase. 

import sys
file = open(sys.argv[1], 'r')
result = []
for line in file.readlines():
	print line.lower(),

file.close()