class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        array = [celsius + 273.15, celsius * 1.80 + 32.00]
        return array