from random import randint 

num1=randint(1,10)
num2=randint(1,10)
mul=1
while True:
    if mul*num1 % num2 == 0:
        lcm = mul*num1
        break
    mul+=1

print "First number is: ", num1
print "Second number is: ", num2
print "L.C.M: ", lcm
