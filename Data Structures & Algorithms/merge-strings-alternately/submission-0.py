class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        res = []
        i = 0
        while p1 < len(word1) and p2 < len(word2):
            if i % 2 == 0:
                res.append(word1[p1])
                p1 += 1
            else:
                res.append(word2[p2])
                p2 += 1
            i += 1
        if p1 < len(word1):
            res.append(word1[p1:])
        if p2 < len(word2):
            res.append(word2[p2:])
        return "".join(res)