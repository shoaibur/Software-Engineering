class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        '''
        T: O(n^2) and S: O(n)
        '''
        nums = []
        def getNums(head):
            tail = head
            while tail:
                nums.append(tail.val)
                tail = tail.next
        
        def insertionSort(nums):
            i = 1
            while i < len(nums):
                j = i - 1
                while j >= 0:
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    j -= 1
                i += 1
        
        if not head: return None
        getNums(head)
        insertionSort(nums)
        for i, num in enumerate(nums):
            if i == 0:
                head = ListNode(num)
                tail = head
            else:
                tail.next = ListNode(num)
                tail = tail.next
        
        return head

    
    
    
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()

        curr = head
        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev_node = pseudo_head
            next_node = prev_node.next
            # find the position to insert the current node
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next

            next_iter = curr.next
            # insert the current node to the new list
            curr.next = next_node
            prev_node.next = curr

            # moving on to the next iteration
            curr = next_iter

        return pseudo_head.next
