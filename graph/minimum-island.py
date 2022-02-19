grid = [['W','L','W','W','L','W'], ['L','L','W','W','L','W'],['W','L','W','W','W','W'],['W','W','W','L','L','W'],['W','L','W','L','L','W'],['W','W','W','W','W','W']]

def islandMin(grid):
    
    smallest = len(grid)*len(grid[0])
    
    visited=set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            size = explore(grid,i,j,visited) 
               
            if size < smallest and size>0:
                smallest = size

    return smallest

def explore(grid,row,col,visited):
    
    if row < 0 or row > len(grid):
        return 0
    
    if col < 0 or  col > len(grid[0]):
        return 0

    if grid[row][col] == 'W':
        return 0
    
    if (row,col) in visited:
        return 0
    visited.add((row,col))
    size = 1
    size += explore(grid,row-1,col,visited)
    size += explore(grid,row+1,col,visited)
    size += explore(grid,row,col-1,visited)
    size += explore(grid,row,col+1,visited)

    return size

print(islandMin(grid))
