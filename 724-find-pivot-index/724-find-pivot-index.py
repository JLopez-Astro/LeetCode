class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # print(nums)
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i:]) - nums[i]
            # print(leftsum)
            # print(rightsum)
            if leftsum == rightsum:
                return i
        return -1
            # else:
            #     continue