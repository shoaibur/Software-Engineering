class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
             up
        left    right
             down
        '''
        currFace = 'up'
        currPos = (0,0)
        
        visited = set()
        
        for instruction in instructions:
            i, j = currPos
            visited.add((i, j))
            if instruction == 'G':
                if currFace == 'up': currPos = (i-1, j)
                elif currFace == 'down': currPos = (i+1, j)
                elif currFace == 'left': currPos = (i, j-1)
                elif currFace == 'right': currPos = (i, j+1)
            elif instruction == 'L':
                if currFace == 'up': currFace = 'left'
                elif currFace == 'left': currFace = 'down'
                elif currFace == 'down': currFace = 'right'
                elif currFace == 'right': currFace = 'up'
            elif instruction == 'R':
                if currFace == 'up': currFace = 'right'
                elif currFace == 'right': currFace = 'down'
                elif currFace == 'down': currFace = 'left'
                elif currFace == 'left': currFace = 'up'
        return currFace != 'up' or currPos == (0,0)
