import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
                continue
            
            if minHeap[0] < num:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)
        minHeap.append(0)
        return minHeap[0]

        