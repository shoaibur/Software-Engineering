## Insertion sort
* Algorithm
  * In: nums array
  * For each item at position i:
    * While item at i-1 > item at i:
      * Swap items between i-1 and i
  * out nums array
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
