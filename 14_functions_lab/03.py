"""
Write a function that calculates the sum
of the 10th digit from all arguments passed to it
"""

def asarotcount(*numbers):
    count = 0
    for num in numbers:
        count += int(str(num)[-2])
    return count


print asarotcount(120, 230, 1150)
