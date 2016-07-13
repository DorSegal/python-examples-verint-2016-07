import sys

hostsfile = {}

with open("hosts", "r") as fin:
    for line in fin:
       (name, ip) = line.split('=')
       hostsfile[name] = ip


for name in sys.argv[1:]:
    try:
        print "%s = %s" % (name, hostsfile[name])

    except:
        print "%s does not exist\n" % name