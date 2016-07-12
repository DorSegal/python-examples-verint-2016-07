import argparse

parser = argparse.ArgumentParser(description="this progem copy contect from source file to destination file")
parser.add_argument("srcfile", type=str ,help="the source file you want to copy")
parser.add_argument("dstfile", type=str, help="destination file")
args = parser.parse_args()


with open(args.srcfile, "r") as srcfile:
    with open(args.dstfile, "a") as dstfile:
        for line in srcfile:
            dstfile.write(line)
        dstfile.write("\n")