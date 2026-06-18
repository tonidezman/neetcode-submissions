class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rec(nums, target, low=0, hi=len(nums)-1)
    
    def rec(self, nums, target, low, hi):
        if low > hi:
            return -1
        
        mid = low + (hi - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            low = mid + 1
        return self.rec(nums, target, low, hi)