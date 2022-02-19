edges = [['w','x'],['w','a'],['a','v'],['x','y'],['z','y'],['z','v'],['w','v']]
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

def shortestPath(graph, src, dst):
    visited = set([src])
    queue = [(src,0)]

    while len(queue)>0:
        current, distance = queue.pop(0)
        
        if current == dst:
            return distance
        
        for neighbor in graph[current]:
            if not neighbor in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))
    
    return distance



print(shortestPath(buildGraph(edges),'w','z'))