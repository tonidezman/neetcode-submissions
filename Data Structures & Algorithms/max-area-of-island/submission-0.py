class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def oob(row: int, col: int) -> bool:
            if row < 0 or col < 0:
                return True
            if row >= len(grid) or col >= len(grid[0]):
                return True
            return False

        def mark_and_get_size(row: int, col: int) -> int:
            if oob(row, col) or (row, col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            res = 1
            res += mark_and_get_size(row-1, col)
            res += mark_and_get_size(row+1, col)
            res += mark_and_get_size(row, col+1)
            res += mark_and_get_size(row, col-1)
            return res
        
        res = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited:
                    continue
                if grid[row][col] == 1:
                    res = max(res, mark_and_get_size(row, col))
        return res

