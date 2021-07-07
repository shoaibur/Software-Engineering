# Using python list
def add_one(nums):
    carry = 1
    for num in nums:
        sums, carry = (num+carry)%10, (num+carry)//10
        nums[-1] = sums
        if carry == 0:
            return nums
    if carry == 1:
        return [1] + nums

    
# Using linked list
def add_one(head):
    # Reverse
    rev_head = reverse(head)
    
    # Add one
    tail = rev_head
    while tail:
        if tail.value < 9:
            tail.value += 1
            return reverse(rev_head)
        else:
            tail.value = 0
            carry = 1
        tail = tail.next
    if carry == 1:
        rev_head.prepend(1)
    return reverse(rev_head)

def reverse(head):
    rev_head = None
    tail = head
    while tail:
        rev_head.prepend(tail.value)
        tail = tail.next
    return rev_head
