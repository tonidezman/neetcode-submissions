class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        L, R = 0, 1
        window = {nums[L]}
        while R < len(nums):
            if len(window) >= (k+1):
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
            R += 1
        return False
