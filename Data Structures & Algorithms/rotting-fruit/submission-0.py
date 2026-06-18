from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def oob(r: int, c: int) -> bool:
            if r < 0 or c < 0:
                return True
            if r >= len(grid) or c >= len(grid[0]):
                return True
            return False

        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
        
        visited = set()
        res = 0
        while queue:
            r, c, minutes = queue.popleft()
            if oob(r, c) or (r, c) in visited or grid[r][c] == 0:
                continue
            grid[r][c] = 2
            res = max(res, minutes)
            visited.add((r, c))
            queue.append((r+1, c, minutes+1))
            queue.append((r-1, c, minutes+1))
            queue.append((r, c-1, minutes+1))
            queue.append((r, c+1, minutes+1))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return res
