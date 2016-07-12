import argparse
import sys
from itertools import izip_longest

parser = argparse.ArgumentParser(description="this progem marge two files into destination file")
parser.add_argument("srcfile1", type=str ,help="the first source file")
parser.add_argument("srcfile2", type=str ,help="the second source file")
parser.add_argument("dstfile", type=str, help="destination file containing marge content")

args = parser.parse_args()

with open(args.srcfile1, "r") as srcfile1:
    with open(args.srcfile2, "r") as srcfile2:
        with open(args.dstfile, "w") as dstfile:           
            for line, line2 in izip_longest(srcfile1, srcfile2, fillvalue=""):
                dstfile.write(line + line2)
