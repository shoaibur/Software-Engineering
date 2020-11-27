class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def search(square):
            n, m = len(square), len(square[0])
            if n == m:    # solution found
                ans.append(square)
                return
            req_prefix = ""    # Generate the required prefix
            for i in range(n):
                req_prefix += square[i][n]
            if req_prefix in prefixes:    # Perform backtracking
                all_prefixes = prefixes[req_prefix]
                for prefix in all_prefixes:
                    search(square + [prefix])
            else:    # Kills the current combination
                return
            
        # Generate all possible prefixes
        prefixes = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefixes[word[:i]].append(word)
        
        ans = []
        for word in words:
            search([word])

        return ans
