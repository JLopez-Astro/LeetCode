class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        o = reduce(lambda a, b: a + b, words)
        p = Counter(o)
        for i in p:
            if p[i] % n != 0:
                return False
        return True