class Graph:
    
    def __init__(self):
        self.adj_list = {}

    #Add an edge from src to dst 
    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src]=set()
        if dst not in self.adj_list:
            self.adj_list[dst]=set()

        self.adj_list[src].add(dst)
        

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False

        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        has_path = self.dfs(src, dst, visited)
        return has_path

    def dfs(self, src, dst, visited) -> bool:
        if src == dst :
            return True

        visited.add(src)

        for neighbor in self.adj_list.get(src,[]):
            if neighbor not in visited:
                if self.dfs(neighbor,dst,visited):
                    return True

        return False


