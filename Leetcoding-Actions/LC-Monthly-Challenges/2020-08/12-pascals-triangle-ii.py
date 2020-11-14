class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        row = [1, 1]
        for k in range(2, rowIndex+1):
            currRow = row.copy()
            for i in range(1, len(row)):
                row[i] = currRow[i-1] + currRow[i]
            row.append(1)
        return row
