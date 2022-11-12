class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head):
    cur = head
    result = []
    while cur is not None:
        result.append(cur.val)
        cur = cur.next

    return result


def reverse(head):
    prev = None
    cur = head
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

result = print_list(reverse(a))
print(result)
assert result == ["f", "e", "d", "c", "b", "a"]


p = Node("p")
result = print_list(reverse(p))
print(result)
assert result == ["p"]
