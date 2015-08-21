#Bit Positions
#Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 are 1 based. 
import sys

file = open('test.txt')
for line in file:
	data = line.replace("\n","").split(",")
	a = int(data[1]) 
	b = int(data[2])
	word = bin(int(data[0]))
	if word[-a] == word[-b]:
		sys.stdout.write('true')
	else:
		sys.stdout.write('false')
	print

file.close()