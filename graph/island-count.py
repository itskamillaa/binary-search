grid = [['W','L','W','W','L','W'], ['L','L','W','W','L','W'],['W','L','W','W','W','W'],['W','W','W','L','L','W'],['W','L','W','L','L','W'],['W','W','W','W','W','W']]

def islandCount(grid):
    count = 0
    visited=set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
                
            if explore(grid,i,j,visited) == True:
                count+=1

    return count

def explore(grid,row,col,visited):
    if row < 0 or row > len(grid):
        return False
    
    if col < 0 or  col > len(grid[0]):
        return False

    if grid[row][col] == 'W':
        return False
    #pos = row +','+ col
    if (row,col) in visited:
        return False
    visited.add((row,col))

    explore(grid,row-1,col,visited)
    explore(grid,row+1,col,visited)
    explore(grid,row,col-1,visited)
    explore(grid,row,col+1,visited)

    return True






print(islandCount(grid))
