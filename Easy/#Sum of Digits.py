#Sum of Digits
#Given a positive integer, find the sum of its constituent digits. 

import sys
file = open(sys.argv[1], 'r')
result = []
for line in file.readlines():
	result.append(int(line))

for e in result:
	s = 0
	k = str(e)
	for i in range(0,len(k)):
		s += int(k[i])
	print s

file.close()