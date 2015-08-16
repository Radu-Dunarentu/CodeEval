#Even Numbers
#Write a program which checks input numbers and determines whether a number is even or not. 

import sys
file = open(sys.argv[1], 'r')


for line in file.readlines():
	print '0' if int(line)%2 else '1'  
	
file.close()
