class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_list(head):
    res = 0
    cur = head
    while cur is not None:
        res += cur.val
        cur = cur.next
    return res


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

result = sum_list(a)
print(result)
assert result == 19
