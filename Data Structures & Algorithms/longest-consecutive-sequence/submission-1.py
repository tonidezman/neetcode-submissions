class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for num in nums:
            prev_num = num-1
            if prev_num not in seen:
                curr = 1
                while num+1 in seen:
                    curr += 1
                    num += 1
                res = max(res, curr)
        return res
