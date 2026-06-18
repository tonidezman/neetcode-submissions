class Solution:
    def rob(self, nums: list[int]) -> int:
        return self.dp(i=0, nums=nums, cache={})

    def dp(self, i: int, nums: list[int], cache: dict[int, int]) -> int:
        if i >= len(nums):
            return 0
        if i in cache:
            return cache[i]
        take_i = nums[i] + self.dp(i+2, nums, cache)
        dont_take_i = self.dp(i+1, nums, cache)
        cache[i] = max(take_i, dont_take_i)
        return cache[i]