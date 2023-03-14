class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        print(max(candies))
        return [i+extraCandies >= max(candies) for i in candies]
        # for i in candies:
        #     return [i+extraCandies > max_candies]