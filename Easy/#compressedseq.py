#compressedseq
"""
Challenge Description:

Assume that someone dictates you a sequence of numbers, and you need to write it down. For brevity, he dictates it as follows: first he dictates the number of consecutive identical numbers, and then - the number itself.

For example:
The sequence below

1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2

is dictated as follows:

two times one, three times three, four times two, three times fourteen, three times eleven, one time two

and you have to write down the sequence

2 1 3 3 4 2 3 14 3 11 1 2

Your task is to write a program that compresses a given sequence using this approach.
"""

import sys
file = open('test.txt')
for line in file:
	result = [] #store checked elements here
	data = map(int,line.replace("\n","").split(" ")) #all elements
	#data_copy = list(set(data)) #unique elements unordered
	for e in data:
		if e not in result: #dont repeat elements
			print data.count(e), e,
			result.append(e) #element checked
	print
	

file.close()