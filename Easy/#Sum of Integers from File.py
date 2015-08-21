#Sum of Integers from File
#Print out the sum of integers read from a file. 
import sys
file = open("test.txt")
sum = 0
for line in file:
	sum += int(line)

print sum

file.close()
