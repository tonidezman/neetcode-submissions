from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        for num, count in counter.items():
            arr[count].append(num)
        res = []
        while len(res) < k:
            for i in range(len(arr)-1,-1,-1):
                for num in arr[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

