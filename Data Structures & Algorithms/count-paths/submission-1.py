class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def oob(row: int, col: int) -> bool:
            if row >= m or col >= n:
                return True
            return False

        def countPaths(row: int, col: int) -> int:
            if oob(row, col):
                return 0
            if row == m-1 and col == n-1:
                return 1
            res = 0
            res += countPaths(row+1, col)
            res += countPaths(row, col+1)
            return res

        return countPaths(row=0, col=0)