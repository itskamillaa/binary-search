def buildGraph(edges):
    graph = {}
    for edge in edges:
        if not edge[0] in graph:
            graph[edge[0]]=[]
            
        if not edge[1] in graph:
            graph[edge[1]]=[]

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph

def undirectedPath(graph,src,dst):
    visited = set()
    return helper(graph,src,dst,visited)

def helper(graph,src,dst,visited):
    #check if we alkready visited the node
    if src in visited:
        return False
    #if the node has not been visited, add it to our visited set
    visited.add(src)
    #base case: check if we reached the destination
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if helper(graph, neighbor,dst,visited):
            return True

    return False



edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]
print(undirectedPath(buildGraph(edges),'i','l'))