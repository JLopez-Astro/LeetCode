class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(nums[i]+sum(nums[:i]))
        return lst