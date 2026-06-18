class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(0, 0, m, n, cache={})

    def dp(self, r: int, c: int, m: int, n: int, cache: dict[tuple[int, int], int]) -> int:
        if r == m-1 and c == n-1:
            return 1
        if r == m or c == n:
            return 0

        key = (r, c)
        if key in cache:
            return cache[key]
        down = self.dp(r+1, c, m, n, cache)
        right = self.dp(r, c+1, m, n, cache)
        cache[key] = down + right
        return cache[key]
