class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def append(self, head, value):
        if head is None: return Node(value)
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
        
def traverse_linked_list(head):
    # Time: O(n) & Space: O(n)
    out = []
    tail = head
    while tail:
        out.append(tail.value)
        tail = tail.next
    return out

def convert_array_to_linked_list(nums):
    # O(n) & O(n)
    if not nums: return None
    head = Node(nums[0])
    for num in nums[1:]:
        head.append(head, num)
    return head

def intersection(llist1, llist2):
    # Traverse linked lists
    nums1 = traverse_linked_list(llist1)
    nums2 = traverse_linked_list(llist2)
    
    # Hash maps
    d1, d2 = {}, {}
    for num in nums1:
        d1[num] = d1.get(num, 0) + 1
    for num in nums2:
        d2[num] = d2.get(num, 0) + 1
    
    n = [] # Intersection
    for num in d1:
        if num in d2:
            n.append(num)
    return convert_array_to_linked_list(n)

# Time: O(n+m)
# Space: O(n+m)

def union(llist1, llist2):
    # Traverse linked lists
    nums1 = traverse_linked_list(llist1)
    nums2 = traverse_linked_list(llist2)
    
    # Hash maps
    d1, d2 = {}, {}
    for num in nums1:
        d1[num] = d1.get(num, 0) + 1
    for num in nums2:
        d2[num] = d2.get(num, 0) + 1
    
    u = [] # Union
    for num in d1:
        u.append(num)
    for num in d2:
        if num not in d1:
            u.append(num)
    return convert_array_to_linked_list(u)

# Test 1
nums1 = [3,2,4,35,6,65,6,4,3,21]
nums2 = [6,32,4,9,6,1,11,21,1]

llist1 = convert_array_to_linked_list(nums1)
llist2 = convert_array_to_linked_list(nums2)

u = traverse_linked_list(union(llist1, llist2)) # expected: [3,2,4,35,6,65,21,32,9,1,11]
print('union:', u)
# union: [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]

n = traverse_linked_list(intersection(llist1, llist2)) # expected: [4,6,21]
print('intersection', n)
# intersection [4, 6, 21]

# Test 2
nums1 = []
nums2 = []

llist1 = convert_array_to_linked_list(nums1)
llist2 = convert_array_to_linked_list(nums2)

u = traverse_linked_list(union(llist1, llist2)) # expected: []
print('union:', u)
# union: []

n = traverse_linked_list(intersection(llist1, llist2)) # expected: []
print('intersection', n)
# intersection []

# Test 3
nums1 = [1]
nums2 = []

llist1 = convert_array_to_linked_list(nums1)
llist2 = convert_array_to_linked_list(nums2)

u = traverse_linked_list(union(llist1, llist2)) # expected: [1]
print('union:', u)
# union: [1]

n = traverse_linked_list(intersection(llist1, llist2)) # expected: []
print('intersection:', n)
# intersection: []

