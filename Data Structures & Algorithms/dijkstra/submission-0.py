class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Setup
        # Construct adjacency list from edges
        adj = {}

        #Adjacency list
        # {
        #   v1:[[v2,2],[v3,3]],
        #   v2:[[v3,1]],
        #   v3:[[]]
        # }
        for i in range(n):
            adj[i] = []

        #Edges = [[source, dest, cost]]
        for source,dest,cost in edges:
            adj[source].append([dest,cost])

        #Djikstra using min heap
        #Traverse adjacency list
        #For each vertex add vertex and cost to reach it onto the min heap
        #Keep track of shortest path so far as we add them onto the min heap
        #initialize min heap with src
        shortest = {}
        minheap = [[0,src]]
        while minheap: 
            cost1, vertex1 = heapq.heappop(minheap)

            if vertex1 in shortest:
                continue
            
            shortest[vertex1] = cost1

            for vertex2, cost2 in adj[vertex1]:
                if vertex2 not in shortest:
                    heapq.heappush(minheap, [cost1+cost2,vertex2])

        #Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
