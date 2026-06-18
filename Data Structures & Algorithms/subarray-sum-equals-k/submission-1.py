class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsh = {0:1}
        res = curr_sum = 0
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += hsh.get(diff, 0)
            hsh[curr_sum] = 1 + hsh.get(curr_sum, 0)
        return res