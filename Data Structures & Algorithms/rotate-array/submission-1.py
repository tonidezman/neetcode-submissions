class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums: List[int], l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= len(nums)
        reverse(nums, l=0, r=len(nums)-1)
        reverse(nums, l=0, r=k-1)
        reverse(nums, l=k, r=len(nums)-1)
