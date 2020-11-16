class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Print ll
tail = head
while tail:
    print(tail.value)
    
def append(head, value):
    if head is None:
        return Node(value)
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = Node(value)
    return head
  
def prepend(head, value):
    if head is None:
        return Node(value)
    tail = head
    head = Node(value)
    head.next = tail
    return head
  
def search(head, value):
    if head is None: return False
    tail = head
    while tail:
        if tail.value == value:
            return True
        tail = tail.next
    return False
  
def remove(head, value):
    if head is None: return head
    if head.value == value:
        head = head.next
    tail = head
    while tail:
        if tail.next.value == value:
            tail.next = tail.next.next
            return
        tail = tail.next
    return
  
def pop(head):
    if head is None: return head
    tail = head
    head = tail.next
    return tail.value
