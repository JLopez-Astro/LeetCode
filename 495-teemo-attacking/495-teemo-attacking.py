class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        length = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            length -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return length