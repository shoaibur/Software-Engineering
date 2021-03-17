import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        '''
        T: O(1) and S: O(1)
        '''
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        '''
        T: O(1) and S: O(1)
        '''
        theta = 2 * math.pi * random.random()
        r = self.r * math.sqrt(random.random())
        
        x = r * math.cos(theta) + self.x
        y = r * math.sin(theta) + self.y
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
