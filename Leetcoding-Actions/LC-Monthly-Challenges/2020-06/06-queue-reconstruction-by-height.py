# Suppose you have a random list of people standing in a queue. Each person is described 
# by a pair of integers (h, k), where h is the height of the person and k is the number 
# of people in front of this person who have a height greater than or equal to h. Write 
# an algorithm to reconstruct the queue.
# Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

def queue_reconstruction_by_height(nums):
    # O(n log n)
    nums = sorted(nums, key = lambda x: (-x[0], x[1]))
    p = []
    # O(n^2): Each insert is O(n), which is for each num O(n)
    for num in nums:
        p.insert(num[1], nums)
    return p
  
# Runtime: O(n^2)
# Space: O(n)
