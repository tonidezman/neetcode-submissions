class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in seen:
                return [seen[other_num], i]
            seen[num] = i