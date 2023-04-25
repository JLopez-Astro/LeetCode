class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        amount = []
        for i in nums:
            track = []
            # track.append(j < i for j in nums)
            for j in nums:
                if j < i:
                    track.append(j)
            amount.append(len(track))
        return amount
                