class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits(i: int) -> int:
            res = 0
            while i > 0:
                res += i & 1
                i >>= 1
            return res

        res = []
        for i in range(n+1):
            res.append(count_bits(i))
        return res
