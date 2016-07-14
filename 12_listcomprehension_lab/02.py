"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""
import itertools

lowletters = [chr(l) for l in range(255) if chr(l).islower()]

for letter in itertools.combinations_with_replacement(lowletters, 3): 
        print(''.join(letter))
