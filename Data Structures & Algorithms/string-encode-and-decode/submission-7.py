class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(word)}#{word}" for word in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find num
            j = i + 1
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            # find word
            start = j + 1
            end = start + num
            res.append(s[start:end])
            i = end
        return res
