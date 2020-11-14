class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        Since we have to find the unique pairs, we can consider only
        directional condition, i.e., if 1 and 3 are present in the array,
        then consider only (1,3) but not (3,1). Therefore, the following
        logic works:
        For each i:
            if (nums[i] - k) in nums excluding nums[i]:
                increment count
        '''
        d = collections.defaultdict(list)
        for i,num in enumerate(nums):
            d[num].append(i)
        
        count = 0
        if k == 0:
            for num in d:
                if len(d[num]) > 1:
                    count += 1
        else:
            for i,num in enumerate(d):
                if num - k in d and d[num-k] != i:
                    count += 1
                    print(num, num - k)
        return count
