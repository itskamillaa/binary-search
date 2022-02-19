graph = {'f':['g','i'], 'g':['h'],'h':[],'i':['j','k'],'j':['i'],'k':[]}

def hasPath(gpaph, src, dst):

    #base case: when we reach the destination node
    if src == dst:
        return True
    #check neighbors of source node
    for neighbor in graph[src]:
        #if there is a pth from neighbor of source node to the destination node, then there is a path from source to destination
        if (graph,neighbor, dst):
            return True
    #if there is not path
    return False

print(hasPath(graph, 'f','k'))

