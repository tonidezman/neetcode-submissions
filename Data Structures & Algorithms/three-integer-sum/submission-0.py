class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                # while j < k and nums[j] == nums[j-1]:
                #     j += 1
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return [list(arr) for arr in res]