class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(t,s))) == len(set(t)) == len(set(s))