class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = l = 0

        for i, c in enumerate(s):
            while c in window:
                window.remove(s[l])
                l += 1
            window.add(c)
            res = max(res, len(window))
        return res