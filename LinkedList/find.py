class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def find(head, target):
    cur = head
    while cur is not None:
        if cur.val == target:
            return True
        cur = cur.next

    return False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

res = find(a, "c")
print(res)
assert res == True

res = find(a, "f")
print(res)
assert res == False
