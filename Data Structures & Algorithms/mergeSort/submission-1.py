# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

from collections import deque

def merge(l1, l2):
    l1 = deque(l1)
    l2 = deque(l2)
    res = []
    while l1 and l2:
        if l1[0].key <= l2[0].key:
            res.append(l1.popleft())
        else:
            res.append(l2.popleft())
    res += l1
    res += l2
    return res


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) < 2:
            return pairs
        mid = len(pairs)//2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])
        return merge(left, right)