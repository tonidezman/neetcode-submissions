import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        hsh = {}
        for x, y in points:
            curr = x**2 + y**2
            if not curr in hsh:
                hsh[curr] = []
            if len(arr) < k:
                heapq.heappush(arr, -curr)
                hsh[curr].append([x, y])
                continue
            
            if curr > -arr[0]:
                continue
            
            heapq.heappop(arr)
            heapq.heappush(arr, -curr)
            hsh[curr].append([x,y])

        res = []
        while len(arr) > 0:
            curr = -arr.pop()
            for a in hsh[curr]:
                res.append(a)
                if len(res) == k:
                    return res
        return res

