from random import randint

num = randint(1,100)

while True:
    guess = int(raw_input("Guess the number: "))
    if num == guess:
        print "!OK!"
        break

    cheat = randint(1,10)

    if cheat % 2 == 0:    

        if num < guess:
            print "your guess is BIGGER"
        else:
            print "your guess is SMALLER"
    else:
        if num < guess:
             print "your guess is SMALLER"
        else:
             print "your guess is BIGGER"