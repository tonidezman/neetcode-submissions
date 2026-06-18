from collections import defaultdict

def sorted_word(word: str) -> str:
    return "".join(sorted(list(word)))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            res[sorted_word(word)].append(word)
        return list(res.values())

