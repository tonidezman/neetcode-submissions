from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_max(counter: Counter) -> tuple[int, int]:
            all_count = sum(counter.values())
            max_count = max(counter.values())
            return max_count, all_count - max_count

        counter = Counter()
        res = 0
        l = r = 0
        while r < len(s):
            counter[s[r]] += 1
            r += 1
            valid_chars_count, other_char_count = get_max(counter) # helper
            while (other_char_count) > k:
                counter[s[l]] -= 1
                l += 1
                valid_chars_count, other_char_count = get_max(counter) # helper
            res = max(res, r-l)
        return res


"""
AAABABB
    ^
A: 4
B: 1
"""