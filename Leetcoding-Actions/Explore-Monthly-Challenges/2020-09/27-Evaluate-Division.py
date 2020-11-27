class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Store all relationships into dict
        self.relation = collections.defaultdict(dict)
        for [x, y], value in zip(equations, values):
            self.relation[x][y] = value
            self.relation[y][x] = 1 / value
        
        output = []
        for x, y in queries:
            if {x, y}.issubset(self.relation):
                output.append(self.dfs(x, y, 1, set()))
            else:
                output.append(-1)
        return output            
            
    def dfs(self, cur, target, carry, visited):
        """
        Return target value if find a path, else return -1.
        
        cur: String, current variable
        target: String, target variable
        carry: Float, current target value
        visited: Set, visited variables
        
        """
        # Path found, return target value
        if cur == target:
            return carry
        
        # Add current variable into visited
        visited.add(cur)
        for next_cur, value in self.relation[cur].items():
            if next_cur not in visited:
                ans = self.dfs(next_cur, target, carry * value, visited)
                if ans != -1:
                    return ans
					
		# If not find , return -1
        return -1
