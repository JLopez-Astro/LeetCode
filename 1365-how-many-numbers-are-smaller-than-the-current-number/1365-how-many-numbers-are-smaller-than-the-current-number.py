class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        amount = []
        for i in nums:
            track = []
            for j in nums:
                if j < i:
                    track.append(j)
            amount.append(len(track))
        return amount
                