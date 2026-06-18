import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
        