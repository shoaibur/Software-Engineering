def prisonAfterNDays(cells, N):
    if N == 0: return cells
    
    m = 14 # repeating_days(cells)
    
    N = (N-1) % m + 1
    while N > 0:
        cells = nextday(cells)
        N -= 1
    return cells

def nextday(cells):
    day = [0] * len(cells)
    for i in range(1, len(cells)-1):
        day[i] = 1 - cells[i-1] ^ cells[i+1]
    return day

'''
def repeating_days(self, cells):
    # Repeating days, i.e., repeat pattern after each m days
    day1 = nextday(cells)
    cells = day1
    m = 0
    while True:
        cells = nextday(cells)
        m += 1
        if cells == day1:
            break
    return m
'''
