class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #Intuition: Shortest path uses bfs
        
        #For each row: explore all neighbors right away first instead of going deep
        #Keep a queue for neighbors to explore
        
        #Keep a visited array to make sure we don't traverse the same path multiple times 
        #and to avoid cycles

        #Setup
        ROWS = len(grid)
        COLS = len(grid[0])
        
        neighbors = deque()
        visited = set()
        length_of_path = 0

        neighbors.append((0,0))
        visited.add((0,0))

        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        #Keep exploring the queue of neighbors as long as it's not empty
        while neighbors:

            #O(col_length)
            for _ in range(len(neighbors)):
                row , col = neighbors.popleft()

                #Check if we reached the target grid
                if row == ROWS - 1 and col == COLS -1:
                    return length_of_path

                #BFS
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    #Skip traversing in this direction if we're out of bound 
                    # or we visited the neighbores
                    if (    min(new_row, new_col) < 0 or
                            new_row == ROWS or
                            new_col == COLS or
                            grid[new_row][new_col] == 1 or
                            (new_row, new_col) in visited
                        ):

                        continue

                    neighbors.append((new_row, new_col))
                    visited.add((new_row, new_col))
                
            #Increment length per level
            length_of_path += 1

        return -1
        