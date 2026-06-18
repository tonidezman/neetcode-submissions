def dp(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return dp(n-2) + dp(n-1)

class Solution:
    def climbStairs(self, n: int) -> int:
        return dp(n)