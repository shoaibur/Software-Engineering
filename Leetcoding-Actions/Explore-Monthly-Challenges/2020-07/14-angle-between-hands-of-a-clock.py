class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Degree per minute = 360/60 = 6
        deg_minutes = 6 * minutes
        
        # Degree per hour = 360/12 = 30
        # Hour hand moves degree per minute = 30/60 = 1/2
        deg_hour = 30 * (hour % 12) + 0.5 * minutes
        
        # Difference between hour and minutes hands
        diff = abs(deg_hour - deg_minutes)
        
        # Return the mininum angle between the two hands
        return min(diff, 360-diff)
