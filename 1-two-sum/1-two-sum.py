class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        index_map = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in index_map:
                pair.append(i)
                pair.append(index_map[check])
                break
            else:
                index_map[n] = i
        return pair