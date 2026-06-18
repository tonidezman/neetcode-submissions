from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsh = Counter()
        hsh[0] = 1
        res = curr_sum = 0
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += hsh[diff]
            hsh[curr_sum] = 1 + hsh[curr_sum]
        return res