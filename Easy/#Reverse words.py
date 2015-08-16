#Reverse words
#Write a program which reverses the words in an input sentence. 

import sys
file = open(sys.argv[1], 'r')
result = []
for line in file.readlines():

	result.append(line.replace("\n", "").split(" "))



for e in result:
	e.reverse()
	" ".join(e)
	print " ".join(e)

file.close()