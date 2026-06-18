class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def oob(nums: list[int], curr: int) -> bool:
            if curr < 0 or curr >= len(nums):
                return True
            return False

        # set negative numbers to zero
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for num in nums:
            idx = abs(num) - 1
            if oob(nums, idx):
                continue
            if nums[idx] > 0:
                nums[idx] *= -1
            elif nums[idx] == 0:
                nums[idx] = -1 * (len(nums)+1)

        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        return len(nums) + 1