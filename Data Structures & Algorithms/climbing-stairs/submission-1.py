class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i: int) -> int:
            if i == n:
                return 1
            if i > n:
                return 0
            return dp(i+1) + dp(i+2)
            
        return dp(0)