"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*numbers):
    return sum([num for num in numbers if type(num) == int])

print mysum(10, 20, 30, "test")

def mymul(*numbers):
    if len(numbers) != 0:
        mul = lambda x, y: x*y
        return reduce(mul,[num for num in numbers if type(num) == int])
    else: return 1

print mymul()

print mymul(10, "dor", 10 )