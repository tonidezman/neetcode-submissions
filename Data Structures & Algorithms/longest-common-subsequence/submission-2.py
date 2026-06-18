class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(i: int, j: int) -> int:
            key = (i, j)
            if key in memo:
                return memo[key]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[key] = 1 + dp(i+1, j+1)
            else:
                memo[key] = max(dp(i+1, j), dp(i, j+1))
            return memo[key]

        return dp(i=0, j=0)