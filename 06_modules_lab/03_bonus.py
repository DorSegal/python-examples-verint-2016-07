import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="The path you want to scan")
parser.add_argument("megabytes", type=int, default=0, help="the minimum file size accepted in Megabytes")
args = parser.parse_args()

for root, dirs, files in os.walk(args.path):
    for name in files:
        fullpath = root + '\\' + name
        size = os.path.getsize(fullpath)
        if size > args.megabytes*1048576:
            print r"file '{filename}' is bigger then {minsize}M. Do you wish do delete it?".format(filename =fullpath, minsize=args.megabytes)
            answer = raw_input(r"Y/N: ")
            if answer.lower() == "y":
                os.remove(fullpath)
