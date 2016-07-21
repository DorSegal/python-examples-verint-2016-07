"""
Write a program that reads data
from property files.
Each line in the file can either be:
    An empty line
    A comment line (Start with #)
    A property line (of the form key = value)

Write a program that takes a property file name and key
as command line arguments and prints the requested value
"""
import re
import argparse
from collections import defaultdict


parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="The file you want to scan")
parser.add_argument("key", type=str, help="sreach of key value")
args = parser.parse_args()



dic = defaultdict(list)
with open(args.file, "r") as f:
    for line in f:
        #re.search(r"^\W*number\W*=\W*(.*)', line)
        res = re.search(r"^\W*" + args.key + r'\W*=\W*(.*)', line)
        if res is not None:
            dic[args.key].append(res.group(1))    
            
if dic.get(args.key) is not None:
    for item in dic.get(args.key):
        print item
else:
    print "key not found"
    
