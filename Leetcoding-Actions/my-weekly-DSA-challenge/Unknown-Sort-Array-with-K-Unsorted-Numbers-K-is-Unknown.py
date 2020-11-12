'''
[1, 3, 5, 6, 4, 2, 12]

[4, 2, 1, 3, 5, 6, 12]

[1, 4, 3, 5, 6, 2, 12]

[1 3 5 6 12]
[4 2] - sort
merge
'''



def sortArrayWithKUnsortedNums(nums):
    
    def binarySearch(nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def lis(nums):
        result = []
        for num in nums:
            i = binarySearch(result, num)
            if i == len(result):
                result.append(num)
            else:
                result[i] = num
        return result

    def sortTwoSortedArary(nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        result = []
        while i < n1 or j < n2:
            v1 = nums1[i] if i < n1 else float('inf')
            v2 = nums2[j] if j < n2 else float('inf')

            if v1 < v2:
                result.append(v1)
                i += 1
            else:
                result.append(v2)
                j += 1
        return result

    if len(nums) <= 1: return nums
    
    sortedArray = lis(nums) # O(n)
    unSortedArray = []
    sortedArraySet = set(sortedArray)
    
    k = len(nums) - len(sortedArray)
    for num in nums:
        if num in sortedArraySet: continue
        unSortedArray.append(num)
        if len(unSortedArray) == k: break
    unSortedArray.sort() # O(k log k)
    
    return sortTwoSortedArary(sortedArray, unSortedArray)


nums = [1, 3, 5, 6, 4, 2, 12]
nums = [4, 2, 1, 3, 5, 6, 12]
nums = [1, 4, 3, 5, 6, 2, 12]

print(sortArrayWithKUnsortedNums(nums))
