class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        res = "".join(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != "#":
                j += 1 #此時j == "#"
            length = int(s[i:j])
            i = j + 1
            res.append(s[i: i + length])
            i = i + length
        return res