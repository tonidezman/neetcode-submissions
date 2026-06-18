from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def oob(row: int, col: int) -> bool:
            if row < 0 or col < 0:
                return True
            if row >= len(grid) or col >= len(grid[0]):
                return True
            return False

        queue = deque([(0, 0, 0)])
        visited = set()
        while queue:
            row, col, distance = queue.popleft()
            if oob(row, col) or grid[row][col] == 1 or (row, col) in visited:
                continue
            visited.add((row, col))
            is_last_cell = row == len(grid)-1 and col == len(grid[0])-1
            if is_last_cell:
                return distance
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                queue.append((row+dr, col+dc, distance+1))
        return -1
