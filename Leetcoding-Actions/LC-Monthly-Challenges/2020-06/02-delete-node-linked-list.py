# Original leetcode problem is simple
def delete(node):
    node.value = node.next.value
    node.next = node.next.next

# Now if the linked list/head and the value to the deleted are given:
# head = 1 --> 2 --> 3 --> 4 --> 5
# tail.value = 1    tail.value = 2    tail.value = 3    tail.value = 4    tail.value = 5
# tail.next = {2}   tail.next = {3}   tail.next = {4}   tail.next = {5}   tail.next = None

def delete(head, value): # Limitation: value cannot be the last node's value
    tail = head
    # O(n), O(1)
    while tail:
        it tail.value == value:
            tail.value = tail.next.value
            tail.next = tail.next.next
        tail = tail.next
    return head
