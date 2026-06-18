import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a, b = -heapq.heappop(stones), -heapq.heappop(stones)
            if a == b:
                continue
            diff = abs(a-b)
            heapq.heappush(stones, -diff)
        return abs(stones[0]) if len(stones) >= 1 else 0
            
        