from collections import defaultdict

def my_sort(word: str) -> str:
    return "".join(sorted(list(word)))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            res[my_sort(word)].append(word)
        return list(res.values())