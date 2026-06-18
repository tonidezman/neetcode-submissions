class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            res = max(res, curr)
            if curr < num:
                curr = num
            res = max(res, curr)
        return res