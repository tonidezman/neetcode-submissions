class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        curr_buy = prices[0]
        last_idx = len(prices)-1
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr < curr_buy:
                curr_buy = curr
            elif curr > curr_buy and (
                i == last_idx or
                prices[i+1] < curr
            ):
                res += curr - curr_buy
                if i < last_idx:
                    curr_buy = prices[i+1]
        return res
        
# [7,1,5,3,6,4]
#    ^