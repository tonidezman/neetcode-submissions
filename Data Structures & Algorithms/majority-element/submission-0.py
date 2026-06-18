class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        curr_num = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num == curr_num:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    counter = 1
                    curr_num = num
        return curr_num
