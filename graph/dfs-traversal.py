graph = {'a': ['b','c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [],'f': []}

# def dfsIterative(graph, source):
#     stack = [source]
#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor)
      
#dfsIterative(graph, 'a')

def dfsRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        dfsRecursive(graph, neighbor) 

dfsRecursive(graph,'a')
    