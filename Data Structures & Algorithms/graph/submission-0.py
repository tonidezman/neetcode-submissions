class Graph:
    
    def __init__(self):
        self.hsh = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.hsh:
            self.hsh[src] = set()
        if dst not in self.hsh:
            self.hsh[dst] = set()
        self.hsh[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.hsh:
            return False
        if dst not in self.hsh:
            return False
        if dst in self.hsh[src]:
            self.hsh[src].remove(dst)
            return True
        return False


    def dfs(self, src: int, dst: int) -> bool:
        if src == dst:
            return True

        graph = self.hsh
        for neighbor in graph[src]:
            if self.dfs(neighbor, dst):
                return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst)

