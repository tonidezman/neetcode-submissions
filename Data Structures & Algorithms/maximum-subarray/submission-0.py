class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0
        for num in nums:
            curr = max(curr, 0)
            curr += num
            res = max(res, curr)
        return res


"""
[2,-3,4,-2,2,1,-1,4]
                 ^
8
4
"""