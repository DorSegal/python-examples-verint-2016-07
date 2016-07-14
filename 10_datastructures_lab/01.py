import sys

hostsfile = {}

with open("hosts", "r") as fin:
    for line in fin:
       (name, ip) = line.rstrip('\n').split('=')
       hostsfile[name] = ip

for name in sys.argv[1:]:
    if name in hostsfile:
        print "{0} IP is {1}".format(name, hostsfile[name])
    else:
        print "{0} does not exist".format(name)
