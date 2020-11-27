class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        
        words = string.split()
        
        if len(words) != len(pattern) or not pattern or not string:
            return False
        
        visited = {}
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            elif words[i] not in visited:
                visited[words[i]] = True
                d[pattern[i]] = words[i]
            else:
                return False
        return True
