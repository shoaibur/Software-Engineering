class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0: return cells
        
        m = 14 # self.repeating_days(cells)
        
        N = (N-1) % m + 1
        while N > 0:
            cells = self.nextday(cells)
            N -= 1
        return cells
    
    def nextday(self, cells):
        day = [0] * len(cells)
        for i in range(1, len(cells)-1):
            day[i] = 1 - cells[i-1] ^ cells[i+1]
        return day
    
