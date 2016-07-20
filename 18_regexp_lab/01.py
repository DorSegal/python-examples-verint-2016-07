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

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="The file you want to scan")
parser.add_argument("key", type=str, help="sreach of key value")
args = parser.parse_args()


def getvaule(key, f):
    #(?<=key = ).*
    res = re.search(r"(?<=" + key + r' = ).*', f)
    if res is not None:
        return res.group(0)
    else: return "key not found"

with open(args.file, "r") as f:
    print getvaule(args.key, f.read())
    