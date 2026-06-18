import math

class Solution:
    def can_eat(self, piles, bananas_per_hour, h):
        res = 0
        for pile in piles:
            res += math.ceil(float(pile) / bananas_per_hour)
        return res <= h



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        res =m 
        low, hi = 1, m
        while low <= hi:
            mid = low + (hi - low) // 2
            if self.can_eat(piles, mid, h):
                res = mid
                hi = mid - 1
            else:
                low = mid + 1
        return res