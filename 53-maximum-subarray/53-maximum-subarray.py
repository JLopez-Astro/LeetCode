class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_sum = min(nums)
        current_sum = 0
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            if current_sum > largest_sum:
                largest_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return largest_sum