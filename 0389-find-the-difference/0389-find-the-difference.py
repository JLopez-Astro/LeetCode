class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        bit = 0
        for bitS in s:
            bit ^= ord(bitS)
            print(bit, ord(bitS))
        for bitT in t:
            bit ^= ord(bitT)
            print(bit, ord(bitT))
        return chr(bit)