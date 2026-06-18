class Solution:
    def trap(self, height: List[int]) -> int:
        prev = 0
        left_maxes = [0] * len(height)
        for i, h in enumerate(height):
            left_maxes[i] = prev
            prev = max(prev, h)
        
        prev = 0
        right_maxes = [0] * len(height)
        for i, h in enumerate(reversed(height)):
            right_maxes[i] = prev
            prev = max(prev, h)
        right_maxes = list(reversed(right_maxes))
        
        res = 0
        for i, h in enumerate(height):
            curr = min(left_maxes[i], right_maxes[i]) - h
            if curr > 0:
                res += curr
        # print(left_maxes)
        # print(right_maxes)
        # print(height)
        return res
