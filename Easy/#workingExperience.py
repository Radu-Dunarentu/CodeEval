#working experience
#you are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed. 
months={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

def diff_month(d1, d2):
    return (d1[1] - d2[1])*12 + d1[0] - d2[0]

def adder(d1,d2):
	month = d1[0]
	year = d1[1]
	for i in range(0,diff_month(d2,d1)+1):
		if [month, year] not in dict:
			dict.append([month, year])
		if month == 12:
			year += 1
			month = 1
		else:
			month += 1
	   


import sys

file = open('test.txt')
for line in file:
	dict = []
	data = line.replace('\n',"").split('; ')
	for e in data:
		a = e.split("-") 
		#month_start = a[0][:3]
		#month_end = a[1][:3]
		d1 = [months[a[0][:3]],int(a[0][-4:])]		
		d2 = [months[a[1][:3]],int(a[1][-4:])]
		adder(d1,d2)


	print len(dict)/12


