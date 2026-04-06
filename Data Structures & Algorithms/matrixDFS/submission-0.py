class Solution:

    def countPaths(self, grid: List[List[int]]) -> int:
        #Intuition: counting number of all possible path means we need to use DFS
        #Can use a direction array to help define constraint
        #For dfs , we want to visit each neighbor deeply instead of processing all neighbors in a row
        #Implement using recursion or iteratively using a call stack
        #We need to keep a visited array so we don't visit the same cell twice in a unique path

        visited = set()
        return self.dfsHelper(grid, 0, 0, visited)
    
    def dfsHelper(self, grid:List[List[int]], row: int, col: int, visited:set) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        #Check boundaries first
        #If out of bounds don't increment the path
        #Check if path is not blocked grid[row][col] == 1
        #Check if we already visited the path
        if ( row < 0 or col < 0 or col == COLS or row == ROWS or grid[row][col] == 1 or (row, col) in visited ):
            return 0

        #Found a path, we reached the bottom of the grid
        if row == ROWS - 1 and col == COLS - 1:
            return 1

        visited.add((row,col))

        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for dr , dc in directions :
            count += self.dfsHelper(grid, row +  dr, col + dc, visited)

        visited.remove((row,col))

        return count


        
        