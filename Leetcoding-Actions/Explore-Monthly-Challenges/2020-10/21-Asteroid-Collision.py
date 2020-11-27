class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        T: (n) and S: O(n)
        '''
        stack = []
        
        for asteroid in asteroids:
            # Case 1: Collision occurs
            while stack and (asteroid < 0 and stack[-1] > 0):
                if stack[-1] < -asteroid: # Case 1a: asteroid survives after collision
                    stack.pop()
                    continue
                elif stack[-1] > -asteroid: # Case 1b: stack[-1] survives after collision
                    break
                else: # Case 1c: None survives after collision
                    stack.pop()
                    break
            else: # No collision, both survive
                stack.append(asteroid)
                
        return stack
