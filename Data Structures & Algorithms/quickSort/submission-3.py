# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.rec(pairs, s=0, e=len(pairs)-1)
        return pairs

    def rec(self, pairs: List[Pair], s: int, e: int) -> None:
        if e-s+1 <= 1:
            return
        pivot = pairs[e]
        left = s
        for i in range(s, e):
            if pairs[i].key >= pivot.key:
                continue
            # swap
            pairs[i], pairs[left] = pairs[left], pairs[i]
            left += 1
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.rec(pairs, s, left-1)
        self.rec(pairs, left+1, e)
            