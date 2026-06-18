class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        memo = {}
        def dp(i: int, j: int) -> int:
            key = (i, j)
            if key in memo:
                return memo[key]
            if i == len(a) or j == len(b):
                return 0
            if a[i] == b[j]:
                memo[key] = 1 + dp(i+1, j+1)
            else:
                memo[key] = (
                    max(dp(i+1, j), dp(i, j+1))
                )
            return memo[key]

        return dp(i=0, j=0)
        