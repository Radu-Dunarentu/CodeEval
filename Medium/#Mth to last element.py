#Mth to last element
#Write a program which determines the Mth to the last element in a list. 
import sys
file = open(sys.argv[1], 'r')

result = []
for line in file.readlines():
	result.append(line.replace("\n", "").split(" "))

for e in result:
	if int(e[-1])< len(e):
		print e[-int(e[-1])-1]

file.close()