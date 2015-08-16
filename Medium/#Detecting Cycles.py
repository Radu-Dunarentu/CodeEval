#Detecting Cycles
#Given a sequence, write a program to detect cycles within it. 


import sys

def brent(f, x0, data):
    # main phase: search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0,data)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == lam:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare, data)
        lam += 1

    # Find the position of the first repetition of length lam
    mu = 0
    tortoise = hare = x0
    for i in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare,data)
    # The distance between the hare and tortoise is now lam.

    # Next, the hare and tortoise move at same speed till they agree
    while tortoise != hare:
        tortoise = f(tortoise,data)
        hare = f(hare,data)
        mu += 1
 
    return lam, mu

def next_pos(elem,data):
	pos = data.index(elem)
	return data[pos+1]

file = open(sys.argv[1], 'r')
result = []
for line in file.readlines():
	sentence = line.replace("\n", "").split(" ")
	xo = sentence[0]
	lam, mu = brent(next_pos, xo, sentence)
	for i in range(0,lam):
		print sentence[i+mu],
	print
	
file.close()