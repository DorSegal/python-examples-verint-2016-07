from random import randint 

num1=randint(1,10000)
num2=randint(1,10000)

if num1 > num2:
    greater = num1
else:
    greater =num2

while True:
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1

print "First number is: ", num1
print "Second number is: ", num2
print "L.C.M: ", lcm