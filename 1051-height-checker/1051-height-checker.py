class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        check = []
        for i,j in zip(heights, sorted(heights)):
            check.append(i != j)
        return sum(check)