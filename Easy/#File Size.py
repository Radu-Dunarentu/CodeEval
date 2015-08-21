#File Size
#Print the size of a file in bytes. 

import sys
import os

file = open('test.txt')
path = file.readline()
print os.stat(path).st_size

file.close()