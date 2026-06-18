from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = []
        for num, count in counter.items():
            heapq.heappush(arr, (-count, num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(arr)[1])
        return res
        