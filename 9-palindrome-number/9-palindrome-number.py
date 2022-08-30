class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)[::-1]
        return test == str(x)