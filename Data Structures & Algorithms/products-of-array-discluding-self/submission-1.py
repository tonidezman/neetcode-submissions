class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [None] * len(nums)
        for i in reversed(range(len(nums))):
            if (i+1) == len(nums):
                suffix[i] = 1
                continue
            suffix[i] = suffix[i+1] * nums[i+1]
        
        res = [None] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res