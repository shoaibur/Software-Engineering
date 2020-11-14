class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurance = {char: i for i, char in enumerate(s)}
        
        for i, char in enumerate(s):
            if char in seen: continue
            
            while stack and char < stack[-1] and i < last_occurance[stack[-1]]:
                seen.remove(stack.pop())
            seen.add(char)
            stack.append(char)
            
        return ''.join(stack)
