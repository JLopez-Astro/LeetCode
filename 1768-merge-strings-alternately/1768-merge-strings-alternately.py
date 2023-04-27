class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i = 0
        j = 0
        merge = []
        while i < w1 or j < w2:
            if i < w1:
                merge += word1[i]
                i += 1
            if j < w2:
                merge += word2[j]
                j += 1
        return ''.join(merge)