class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iteration_t = iter(t)
        for i in s:
            if i not in iteration_t:
                return False
        return True