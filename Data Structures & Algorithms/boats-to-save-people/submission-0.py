class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        l, r = 0, len(people)-1
        while l <= r:
            curr = people[l] + people[r]
            if curr > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            res += 1
        return res