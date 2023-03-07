class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        record = []
        for i,row in enumerate(mat):
            record.append((sum(row),i))
        record.sort()
        return [pair[1] for pair in record[:k]]