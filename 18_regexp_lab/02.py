"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""

import re


def toCamelCase(txt):
    res = re.split(r'_',txt)
    string = res[0]
    for item in res[1:]:
        string += re.sub(r'\b\w',
                lambda m: m.group(0).upper()
                , item)
    return string

def toNonCamelCase(txt):
    res = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)',txt)
    string = res[0]
    for item in res[1:]:
        string += '_' + re.sub(r'\b\w',
                lambda m: m.group(0).lower()
                , item)
    return string 


print toCamelCase('welcome') #welcome
print toCamelCase('hello_world') #helloWorld
print toCamelCase('get_name') #getName
print toCamelCase('no_more_shall_we_part') #noMoreShallWePart


print toNonCamelCase('welcome')
print toNonCamelCase('helloWorld')
print toNonCamelCase('getName')
print toNonCamelCase('noMoreShallWePart')