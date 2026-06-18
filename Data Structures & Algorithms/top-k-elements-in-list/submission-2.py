from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = []
        for num, count in counter.items():
            heapq.heappush(arr, (-count, num))
        res = heapq.nsmallest(k, arr)
        return list(map(lambda x: x[1], res))
        