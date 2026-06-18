class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other_nums = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in other_nums:
                return [other_nums[other_num], i]
            other_nums[num] = i