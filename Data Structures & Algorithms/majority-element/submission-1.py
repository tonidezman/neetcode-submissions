class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == res:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    res = nums[i]
                    counter = 1
        return res