class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        left = right = 0
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                swap(nums, left, right) # helper
            right += 1
        return left + 1