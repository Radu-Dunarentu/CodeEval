#Multiples of a Number
#Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator. 
import sys
file = open('test.txt')
for line in file:
	sentence = line.replace("\n","").split(",")
	first = int(sentence[0])
	second = int(sentence[1])
	print 4 if first <= 4 else 8 if first <= 8 else 16 if first <= 16 else 32 if first <= 32 else 64 if first <= 64 else 128 if first <= 128 else 256 if first <= 256 else 512 if first <= 512 else 1024 if first <= 1024 else 2048 if first <= 2048 else 4096 if first <= 4096 else 8192 if first <= 8192 else 16384 if first <= 16384 else 32768

file.close()