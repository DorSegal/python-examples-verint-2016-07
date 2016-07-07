import os
import sys

if len(sys.argv) != 3:
    print "Usage: {0} path minsize".format(sys.argv[0])
    sys.exit(1)


(_, path, minsize) = sys.argv

for root, dirs, files in os.walk(path):
    for name in files:
        fullpath = root + '\\' + name
        size = os.path.getsize(fullpath)
        if size > int(minsize):
            print r"file '{filename}' is bigger then {minsize}. Do you wish do delete it?".format(filename =name, minsize=minsize)
            answer = raw_input(r"Y/N: ")
            if answer.lower() == "y":
                os.remove(fullpath)

