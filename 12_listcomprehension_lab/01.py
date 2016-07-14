"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""

lowletters = [chr(l) for l in range(255) if chr(l).islower()]

print lowletters

