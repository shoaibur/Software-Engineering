def traverse(head):
    out = []
    tail = head
    while tail:
        out.append(tail.value)
        print(tail.value, end=' ')
        tail = tail.next
    return out
