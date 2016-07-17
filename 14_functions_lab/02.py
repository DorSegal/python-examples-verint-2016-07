"""
Write a function that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

def int_string(x, s):
    if type(x) != int: raise ValueError('first must be int')
    if type(s) != str: raise ValueError('second must be string')

int_string("d", "dd")