class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        To put the largest element in the correct place,
        two flips are needed: flip arr[:k] where k is
        index of the largest element and then flip entire arr.
        3 2 4 1
        4 2 3 1 <-- k = 3
        1 3 2 4 <-- k = 4
        ...
        T: O(n^2) and S: O(1)
        '''
        def flip(arr, k):
            arr[:k] = arr[:k][::-1]
        
        result = []
        for num in range(len(arr), 0, -1):
            k = arr.index(num)
            if k != 0:
                flip(arr, k+1)
                result.append(k+1)
            flip(arr, num)
            result.append(num)
            
        return result
