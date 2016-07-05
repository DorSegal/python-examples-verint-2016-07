print "This program will get10 numbers for user and return the biggset one"

i=0
number=0
temp=0
for i in range(0,10):
    print "Please enter number:",
    temp=int(raw_input())
    if number < temp: number=temp
    print

print number


