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
            num = int(s[i:j])
            i = j + 1
            word = s[i:i+num]
            res.append(word)
            i += num
        return res