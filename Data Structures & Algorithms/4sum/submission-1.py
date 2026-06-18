class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                l, r = j+1, len(nums)-1
                while l < r:
                    curr = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif curr < target:
                        l += 1
                    else:
                        r -= 1
        return [list(arr) for arr in res]