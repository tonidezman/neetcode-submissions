from collections import deque

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        window = deque()
        j = 0
        for i in range(len(nums)):
            # until the window is at k size 
            window.append(nums[i])
            window_size = i-j+1
            if window_size < k:
                continue
            res = min(res, max(window)-min(window))
            window.popleft()
            j += 1
        return res
