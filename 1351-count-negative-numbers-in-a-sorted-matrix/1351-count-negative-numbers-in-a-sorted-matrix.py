class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = []
        for i in grid:
            for j in i:
                if j<0:
                    negatives.append(j)
        return len(negatives)