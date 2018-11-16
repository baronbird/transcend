import sys, random



def dfs_rec(curr, stack):
    visited.add(curr)
    if not len(edges[curr]):
        stack.pop()
        return
    for vertex in edges[curr]:
        # Check for cycles and do not add if already in stack
        if vertex not in stack:
            stack.append(vertex)
            dfs_rec(vertex, stack)
    stack.pop()
    return



nodes = set()
visited = set()
edges = {}
for line in open(sys.argv[1]):
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

print "Graph processed, starting search"

connComponents = 0
largestComponent = 0
prevLen = 0

while (len(nodes - visited) > 0):

    stack = random.sample(nodes - visited, 1)
    dfs_rec(stack[0], stack)
    connComponents = connComponents + 1
    if len(visited) - prevLen > largestComponent:
        largestComponent = len(visited) - prevLen
    print "Found Connected Component of size: ", len(visited) - prevLen
    prevLen = len(visited)

print "Largest Connected Component: ", largestComponent
print "Number of Connected Components: ", connComponents
