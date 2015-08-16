#longest Lines
#Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based on their length in descending order. 
import sys
file = open(sys.argv[1], 'r')
count = int(file.readline())
result = {}
for line in file.readlines():
	sentence = line.replace("\n", "")
	result[sentence] = len(sentence)

keys = sorted(result.values())

def key_for_value(dict, value):
    """Return a key in `d` having a value of `value`."""
    for k, v in dict.iteritems():
        if v == value:
            return k	

for i in range(1,count+1):
	print key_for_value(result, keys[-i])
	
file.close()