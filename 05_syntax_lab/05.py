from random import randint
while True:
    number =randint(1,1000000)
    if number % 7 == 0 and number % 15 == 0 and number % 13 == 0:
        print number
        break  