class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in reversed(range(0, 32)):
            res |= (n & 1) << i
            n >>= 1
        return res