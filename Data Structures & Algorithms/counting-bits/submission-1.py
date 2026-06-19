def count_bits(num: int) -> num:
    return bin(num).count('1')

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            res.append(count_bits(num))
        return res