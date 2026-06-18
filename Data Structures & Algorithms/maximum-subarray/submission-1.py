class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr += num
            curr = max(num, curr)
            res = max(res, curr)
        return res
