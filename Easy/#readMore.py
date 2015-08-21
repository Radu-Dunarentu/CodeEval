#readMore

import sys
file = open('test.txt')
for line in file:
	data = line.replace('\n','')
	if len(data) <= 55:
		print data
	else:
		new_line = data[:40] #trim
		new_line = new_line[::-1] #reverse 
		pos = new_line.find(" ") # find pos of space 
		final_line = new_line[pos+1:] #trim everyting until you find space
		print final_line[::-1] + '... <Read More>' #reverse back and print

