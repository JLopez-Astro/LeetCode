class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(str(i) for i in digits)) + 1
        digits = list(str(digits))
        final = [int(i) for i in digits]
        return digits