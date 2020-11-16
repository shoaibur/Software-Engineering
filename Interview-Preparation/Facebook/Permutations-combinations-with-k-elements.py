class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        '''Generate all combinations and get those with k elements'''
        # nums = range(1, n+1)
        # out = [[]]
        # for num in nums:
        #     for item in out:
        # result = []
        # for item in out:
        #     if len(item) == k:
        #         result.append(item)
        # return result
        
        '''Skip combinations with more than k elements'''
        nums = range(1, n+1)
        result = []
        out = [[]]
        for num in nums:
            temp = []
            for item in out:
                comb = item + [num]
                if len(comb) == k:
                    result.append(comb)
                else:
                    temp.append(comb)
            out += temp
        return result
        
        '''Using stack'''
        # # nums = range(1, n+1)
        # combinations = []
        # q = collections.deque()
        # q.append(([], 0))
        # while q:
        #     temp, curr = q.popleft()
        #     if len(temp) == k:
        #         combinations.append(temp)
        #         continue # no need to consider if already more than k elements
        #     for i in range(curr, n):
        #         q.append((temp+[i+1], i+1))
        #         # q.append((temp+[nums[i]], i+1))
        # return combinations
