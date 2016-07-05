from random import randint 

total = 0
for i in range(0,7):
    total += randint(1,100)
print total
if total % 7 == 0:
    print "Boom"
