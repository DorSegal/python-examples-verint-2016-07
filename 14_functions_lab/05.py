"""
Write a function groupby that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""
from collections import defaultdict
def groupby(func, *words):
    milon = defaultdict(list)
    for word in words: milon[func(word)].append(word)
    return milon


# returns: { h: [‘hello’, ‘hi’, ‘help’, ‘here’], b: [‘bye’] }
groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')