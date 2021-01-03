class Solution:
    def countArrangement(self, n: int) -> int:
        # using a recursive function we start from n and move towards 1 to ensure all elements are placed according to the condition
        #the 'used' array is used to keep track of the indices in which elements are placed
        used=[False for i in range(n+1)]
        count = 0
        def backtrack(num = 1):
            nonlocal count
            if num == n+1:
                count += 1 #if we have placed all the elements
                return
            
            for i in range(1, n+1):
                if not used[i] and (num % i == 0 or i % num == 0): #if the index i is free and either i divides x or x divides i
                    used[i] = True
                    backtrack(num + 1) #Recursion for x-1 element to be placed
                    used[i] = False        #backtracking 
        backtrack()
        return count
