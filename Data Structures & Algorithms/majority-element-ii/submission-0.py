from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        for num, count in counter.items():
            if count > (len(nums) // 3):
                res.append(num)
        return res
