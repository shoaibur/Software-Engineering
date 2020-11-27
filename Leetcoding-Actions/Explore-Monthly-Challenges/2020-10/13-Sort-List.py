# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        # Sorting code (merge sort)
        def mergeSort(nums):
            # Divide
            def divide(nums):
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]
                return left, right
            # Merge
            def mergeSortedLists(left, right):
                merged = []
                nLeft, nRight = len(left), len(right)
                i, j = 0, 0
                while i < nLeft or j< nRight:
                    vLeft = left[i] if i < nLeft else float('inf')
                    vRight = right[j] if j < nRight else float('inf')
                    
                    if vLeft < vRight:
                        merged.append(vLeft)
                        i += 1
                    else:
                        merged.append(vRight)
                        j += 1
                return merged
            # Divide, sort and merge
            if len(nums) <= 1: return nums
            left, right = divide(nums)
            left = mergeSort(left)
            right = mergeSort(right)
            return mergeSortedLists(left, right)
        
        # Items in LL
        nums = []
        tail = head
        while tail:
            nums.append(tail.val)
            tail = tail.next
        # Sort
        nums = mergeSort(nums)
        # nums.sort()
        
        # Create LL from sorted items
        new_head = ListNode(0)
        tail = new_head
        for num in nums:
            tail.next = ListNode(num)
            tail = tail.next
        return new_head.next
