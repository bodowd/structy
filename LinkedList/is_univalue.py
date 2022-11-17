class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_univalue(head):
    cur = head
    while cur is not None:
        # value should always be the same as the head node value
        if cur.val != head.val:
            return False
        cur = cur.next

    return True


a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

result = is_univalue(a)
print(result)
assert result == True


a = Node(7)
b = Node(7)
c = Node(9)

a.next = b
b.next = c

result = is_univalue(a)
print(result)
assert result == False
