class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        window = set()
        for i, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            res = max(res, i - left + 1)
        return res


"""
{y }
"zxyzxyz"
       ^
    ^
"""