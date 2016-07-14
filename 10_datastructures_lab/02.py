from collections import defaultdict

anagrams = defaultdict(str)

with open("file.txt" ,"r") as fin:
    for line in fin:
        word = line.rstrip("\n")
        key = ''.join(sorted(word.lower()))
        anagrams[key] += word + " "

for item in anagrams:
    print anagrams[item]
