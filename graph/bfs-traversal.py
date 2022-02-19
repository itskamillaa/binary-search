graph = {'a': ['b','c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [],'f': []}

def bfsIterative(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
      
bfsIterative(graph, 'a')




    