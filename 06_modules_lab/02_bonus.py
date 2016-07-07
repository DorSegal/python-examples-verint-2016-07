import sys

if len(sys.argv) != 3:
    print "Usage: {0} num1 num2".format(sys.argv[0])
    sys.exit(1)

try: 
    print int(sys.argv[1]) + int(sys.argv[2])
    sys.exit(1)

except ValueError:
    print "Only allowed numbers"
    sys.exit(1)



