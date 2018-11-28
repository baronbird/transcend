import sys
import random
import glob

'''
To generate stats for networks with directory structure:
networks
|
|-- subfolder
    |
    |-- networks.txt

run command 'python netStats.py networks/*/*.txt'
'''

def usage(exit_code=0):
	print "Usage: {} INPUT_FILE".format(sys.argv[0])
	sys.exit(exit_code)

if len(sys.argv) != 2:
    usage(1)

for f in glob.glob(sys.argv[1]):
    nodes = set()
    numEdges = 0
    for line in open(f):
        numEdges = numEdges + 1
        curr = line.split()

        nodes.add(curr[0])
        nodes.add(curr[1])

    print "Network: {}".format(f)
    print "Nodes:", len(nodes)
    print "Edges:", numEdges
