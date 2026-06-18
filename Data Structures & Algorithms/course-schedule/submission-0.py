
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites) # helper
        visiting = set()
        visited = set()
        for node in graph:
            if self.hasCycle(graph, node, visiting, visited):
                return False
        return True

    def hasCycle(self, graph: dict[int, set[int]], node: int, visiting: set, visited: set) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for neighbor in graph[node]:
            if self.hasCycle(graph, neighbor, visiting, visited):
                return True
        visiting.remove(node)
        visited.add(node)
        return False
        
    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> dict[int, set[int]]:
        res = {}
        for course in range(numCourses):
            res[course] = set()
        for a, b in prerequisites:
            res[a].add(b)
        return res
