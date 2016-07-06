print "This program will get10 numbers for user and return the biggset one"

number=0
for i in range(0,10):
    temp=int(raw_input("Please enter number:"))
    if number < temp: number=temp
print number





