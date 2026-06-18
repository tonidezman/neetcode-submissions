class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def swap(arr: List[int], i: int, j:int) -> None:
            arr[i], arr[j] = arr[j], arr[i]
           
        l_bound = 0
        r_bound = len(nums)-1
        i = 0

        while i <= r_bound:
            num = nums[i]
            if num == 1:
                i += 1
            elif num == 0:
                swap(nums, i, l_bound)
                l_bound += 1
                i += 1
            elif num == 2:
                swap(nums, i, r_bound)
                r_bound -= 1


