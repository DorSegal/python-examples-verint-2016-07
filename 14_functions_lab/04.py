"""
Write a function that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(length, *words):
    return [word for word in words if len(word) > length]


print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')