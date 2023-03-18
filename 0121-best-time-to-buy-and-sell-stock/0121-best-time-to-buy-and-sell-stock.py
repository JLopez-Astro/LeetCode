class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most, least = 0, float('inf')
        for i in prices:
            least = min(least,i)
            diff = i - least
            most = max(most, diff)
        return most