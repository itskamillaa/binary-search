def connectedComponents(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited) == True:
            count+=1
    return count

def explore(graph, src, visited):
    if src in visited:
        return False
    visited.add(src)

    for neigbor in graph[src]:
        explore(graph,neigbor,visited)

    return True



graph ={1:[2],2:[1],3:[],4:[6],5:[6],6:[4,5,7,8],7:[6],8:[6]}
print(connectedComponents(graph))
    