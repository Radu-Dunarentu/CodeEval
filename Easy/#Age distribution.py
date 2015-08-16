#Age distribution
# You're responsible for providing a demographic report for your local school district based on age. To do this, you're going determine which 'category' each person fits into based on their age.

The person's age will determine which category they should be in:

If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms'
If they're 3 or 4 and should be in preschool print : 'Preschool Maniac'
If they're from 5 to 11 and should be in elementary school print : 'Elementary school'
From 12 to 14: 'Middle school'
From 15 to 18: 'High school'
From 19 to 22: 'College'
From 23 to 65: 'Working for the man'
From 66 to 100: 'The Golden Years'
If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"

import sys
file = open(sys.argv[1], 'r')




for line in file.readlines():
    if int(line) < 0:
        print 'This program is for humans'
    else:
	    print 'Still in Mama\'s arms' if int(line) < 3 else 'Preschool Maniac' if int(line) < 5 else 'Elementary school' if int(line) < 12 else 'Middle school' if int(line) < 15 else 'High school' if int(line) < 19 else 'College' if int(line) < 23 else 'Working for the man' if int(line) < 66 else 'The Golden Years' if int(line) < 101 else 'This program is for humans'
	
file.close()