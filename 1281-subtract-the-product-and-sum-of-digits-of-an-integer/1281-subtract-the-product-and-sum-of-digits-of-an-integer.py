class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(x) for x in str(n)]
        sum_nums = sum(nums)
        prod = 1
        for i in nums:
            prod = prod*i
        return prod-sum_nums