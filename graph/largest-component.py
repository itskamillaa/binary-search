def connectedComponents(graph):
    visited = set()
    
    largest = 0
    for node in graph:
        size = explore(graph,node,visited)
        if size > largest:
            largest = size
            
    return largest

def explore(graph, current, visited):
    
    if current in visited:
        return 0
    visited.add(current)
    nodes = 1
    
    for neighbor in graph[current]:
        nodes += explore(graph, neighbor, visited)
        
    
    return nodes


graph ={1:[2],2:[1],3:[],4:[6],5:[6],6:[4,5,7,8],7:[6],8:[6]}
print(connectedComponents(graph))
    