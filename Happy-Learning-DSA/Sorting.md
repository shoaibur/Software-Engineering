## Insertion sort
* Algorithm
  * Input: nums array
  * For each item at position i:
    * While item at i-1 > item at i:
      * Swap items between i-1 and i
  * Output: nums array
  ```
  def insertion(nums):
      n = len(nums)
      for i in range(1, n):
          j = i
          while j > 0 and nums[j-1] > nums[j]:
              nums[j-1], nums[j] = nums[j], nums[j-1]
              j -= 1
      return nums
  ```
* Complexity analysis
  * Time complexity: n-1 steps in the loop; maximum of n-1 compare and swap in each step. Therefore,
    * T(n) = T(n-1) * T(n-1) = O(n^2)
  * Space complexity: in-place. O(1)


## Selection sort
* Algorithm
  ```
  def selectionSort(nums):
    '''
    Keep track of current position starting from the left and
    swap its element with the min from its right.
    T: O(n^2)
    S: O(1)
    '''
    curPosition = 0
    while curPosition < len(nums):
        unsortedPart = nums[curPosition:]
        minIndex = unsortedPart.index(min(unsortedPart)) + curPosition
        nums[curPosition], nums[minIndex] = nums[minIndex], nums[curPosition]
        curPosition += 1
        
    return nums
  ```
* Complexity analysis

## Bubble sort
* Algorithm
  ```
  def bubbleSort(nums):
    '''
    T: O(n^2)
    S: O(1)
    '''
    lastPosition = len(nums) - 1
    
    while True:
        countSwap = 0
        i = 1
        
        while i <= lastPosition:
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                countSwap += 1
            i += 1
            
        lastPosition -= 1
        if countSwap == 0: break
            
    return nums
  ```
* Complexity analysis


## Merge Sort
* Algorithm
  * Input: nums array
  * func mergeSort(nums):
    * left, right = divide(nums)
    * left = mergeSort(left)
    * right = mergeSort(right)
    * mergedSorted = merge(left, right)
  * Output: mergedSorted
  ```
  def mergeSort(nums):
      if len(nums) <= 1: return nums
      
      def divide(nums):
          mid = len(nums) // 2
          left = nums[:mid]
          right = nums[mid:]
          return left, right
          
      def merge(left, right):
          nLeft = len(left)
          nRight = len(right)
          mergedSorted = []
          i, j = 0, 0
          while i < nLeft or j < nRight:
              vLeft = left[i] if i < nLeft else float('inf')
              vRight = right[j] if j < nRight else float('inf')
              if vLeft < vRight:
                  mergedSorted.append(vLeft)
                  i += 1
              else:
                  mergedSorted.append(vRight)
                  j += 1
          return mergedSorted
      
      left, right = divide(nums)
      left = mergeSort(left)
      right = mergeSort(right)
      mergedSorted = merge(left, right)
      return mergedSorted
  ```
  
  * Complexity analysis
  * Time complexity: Consider a tree with
    * T(n) = O(1) + 2T(n/2) * O(n), i.e. divide + merge sort + merge = O(n log n)
    * Explanation:
      * At level 0, total number of operations = n
      * At level 1, total number of operations = n/2 + n/2 = n
      * At level 2, total number of operations = n/4 + n/4 + n/4 + n/4 = n
      * ...
      * At final level, total number of operations = 1 + 1 + ... + 1 = n
      * Number of levels = height or depth of the tree = 1 + log n
      * Therefore, O( (1 + log n) * n ) = O(n log n)
  * Space complexity: Auxiliary space required for left and right arrays, so O(n).


## Quick sort
* Algorithm
  ```
  ```
* Complexity analysis

## Counting sort
* Algorithm
  ```
  def countingSort(nums):
    if len(nums) <= 1: return nums
    
    # Initialize the counter with all zeros
    minNum, maxNum = min(nums), max(nums)
    counter = {}
    for num in range(minNum, maxNum+1):
        counter[num] = 0
        
    # Count the numbers in nums
    for num in nums:
        counter[num] += 1
    
    # Computer cumulative sum of the counter
    # Key = number in nums; Value = index of the numbers in nums
    curCount = 0
    for num in counter:
        counter[num] += curCount
        curCount = counter[num]
    
    # Sort numbers in nums
    sortedNums = [0] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        index = counter[num] - 1
        sortedNums[index] = num
        counter[num] -= 1
    
    return sortedNums
  ```
* Complexity analysis


## Radix sort
* Algorithm
  ```
  ```
* Complexity analysis

## Bucket sort
* Algorithm
  ```
  import collections

  def bucketSort(nums):
    '''
    T: O(n*d); n=#items in nums, d=#digt in max num
    S: O(n*d)
    '''
    # Get number of digits in max num and convert each number equal to that number of digits
    maxNum = max(nums)
    maxDigit = len(str(maxNum))
    nums = ['0'*(maxDigit-len(str(num)))+str(num) for num in nums]
    
    # Put the numbers into buckets according to its digit (least to most significant)
    for digit in range(maxDigit-1, -1, -1):
        # Init buckets and fill it
        buckets = collections.defaultdict(list)
        for num in nums:
            buckets[num[digit]].append(num)
        # Sorted nums based on curret digit
        nums = []
        for bucket in buckets:
            nums.extend(buckets[bucket])
    # Convert each number into int again
    nums = [int(num) for num in nums]
    
    return nums
  ```
* Complexity analysis


## Heap sort
* Algorithm
  ```
  import heapq
  def heapSort(nums):
    '''
    T: O(n log n)
    S: O(n)
    '''
    sortedNums = []
    
    while nums:
        heapq.heapify(nums)
        sortedNums.append(nums.pop(0))
    
    return sortedNums
  ```
* Complexity analysis
