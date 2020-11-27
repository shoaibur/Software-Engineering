class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        T: O(n) and S: O(n)
        '''
        # Start with all poured into the first cup (at 0th row)
        cups = [poured]
        
        for i in range(query_row):
            # Number of cups in next row (1 more than current row)
            new_cups = [0] * (len(cups) + 1)
            
            # Loop through each cup and measure the overflow
            for j in range(len(cups)):
                # Overflow is anything a cup can't hold, i.e. amount - 1, but can't be negative.
                over_flow = max(0, cups[j] - 1)
                
                # Overflow is equally divided into adjacent cups in next row
                new_cups[j] += over_flow / 2
                new_cups[j + 1] += over_flow / 2
            # Update cups
            cups = new_cups
            
        return min(1, cups[query_glass])
