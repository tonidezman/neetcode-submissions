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
            # get num
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            # get word
            start = j + 1
            end = start + num
            res.append(s[start:end])
            i = end
        return res
