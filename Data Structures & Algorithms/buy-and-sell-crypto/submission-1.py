class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = r = 0
        for i, price in enumerate(prices):
            if price < prices[l]:
                l = i
            r = i
            res = max(res, prices[r] - prices[l])
        return res
            