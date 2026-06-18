class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def oob(grid, row, col):
            if row < 0 or col < 0:
                return True
            if row >= len(grid) or col >= len(grid[0]):
                return True
            return False

        def dfs(row: int, col: int) -> None:
            if oob(grid, row, col) or grid[row][col] == 1 or (row, col) in visiting:
                return 0
            is_last_cell = row == len(grid)-1 and col == len(grid[0])-1
            if is_last_cell:
                return 1
            visiting.add((row, col))
            res = 0
            res += dfs(row-1, col)
            res += dfs(row+1, col)
            res += dfs(row, col+1)
            res += dfs(row, col-1)
            visiting.remove((row, col))
            return res
        visiting = set()
        return dfs(row=0, col=0)