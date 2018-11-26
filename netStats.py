import sys, random


def usage(exit_code=0):
	print "Usage: {} INPUT_FILE".format(sys.argv[0])
	sys.exit(exit_code)

if len(sys.argv) != 2:
    usage(1)

print "Counting nodes and edges..."

nodes = set()
visited = set()
edges = {}
numEdges = 0
for line in open(sys.argv[1]):
    numEdges = numEdges + 1
    curr = line.split()
    if curr[0] not in edges.keys():
        edges[curr[0]] = set()
    edges[curr[0]].add(curr[1])
    if curr[1] not in edges.keys():
        edges[curr[1]] = set()
    edges[curr[1]].add(curr[0])

    nodes.add(curr[0])
    nodes.add(curr[1])

print "Nodes:", len(nodes)
print "Edges:", numEdges
