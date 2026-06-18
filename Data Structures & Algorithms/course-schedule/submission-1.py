class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def buildGraph(numCourses: int, prerequisites: list[list[int]]) -> dict[int, list[int]]:
            res = {}
            for course in range(numCourses):
                res[course] = []
            for a, b in prerequisites:
                res[a].append(b)
            return res

        def hasCycle(node: int) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            for neighbor in graph[node]:
                if hasCycle(neighbor):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        graph = buildGraph(numCourses, prerequisites)
        visiting, visited = set(), set()
        for node in range(numCourses):
            if hasCycle(node):
                return False
        return True