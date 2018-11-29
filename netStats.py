import sys
import random
import glob
import argparse

'''
To generate stats for networks with directory structure:
networks
|
|-- subfolder
    |
    |-- networks.txt

run command 'python netStats.py networks/*/*.txt'
'''

parser = argparse.ArgumentParser(description='Generate network stats from network files')

parser.add_argument('indir', metavar='INPUT_DIR', type=str)

args = parser.parse_args()

count = 0

for f in glob.glob(args.indir):
    nodes = set()
    numEdges = 0
    for line in open(f):
        numEdges = numEdges + 1
        curr = line.split()

        nodes.add(curr[0])
        nodes.add(curr[1])

    count = count + 1

    print "Network: {}".format(f)
    print "Nodes:", len(nodes)
    print "Edges:", numEdges

print "Processed {} total networks".format(count)
