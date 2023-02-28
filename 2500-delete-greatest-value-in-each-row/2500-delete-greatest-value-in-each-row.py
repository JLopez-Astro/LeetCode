class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        grid = list(zip(*grid))
        return sum(max(j) for j in grid)