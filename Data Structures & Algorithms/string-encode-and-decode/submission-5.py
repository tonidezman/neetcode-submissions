class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{len(word)}:{word}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # we need to get num
            j = i + 1
            while s[j] != ":":
                j += 1
            num = int(s[i:j])
            start = j + 1
            end = start + num
            res.append(s[start:end])
            i = end
        return res
        