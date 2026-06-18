class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{len(word)}#{word}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # get number
            j = i
            while s[j] != "#":
                j += 1
            offset = int(s[i:j])
            start = j + 1
            end = start + offset
            # get word
            res.append(s[start:end])
            i = end
        return res