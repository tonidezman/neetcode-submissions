class Solution:
    def oob(self, grid: List[List[str]], r: int, c: int) -> bool:
        if r < 0 or c < 0:
            return True
        if r >= len(grid) or c >= len(grid[0]):
            return True
        return False

    def mark(self, grid: List[List[str]], r: int, c: int, marker: str) -> None:
        if self.oob(grid, r, c) or grid[r][c] == "0" or grid[r][c] == marker:
            return
        grid[r][c] = marker
        self.mark(grid, r-1, c, marker)
        self.mark(grid, r+1, c, marker)
        self.mark(grid, r, c+1, marker)
        self.mark(grid, r, c-1, marker)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cell = grid[r][c]
                if cell == "1":
                    res += 1
                    self.mark(grid, r, c, marker="X")
        return res
        