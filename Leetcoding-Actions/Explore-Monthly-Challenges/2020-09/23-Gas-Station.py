class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        total_tank, curr_tank = 0, 0
        start = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                start = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return start if total_tank >= 0 else -1
