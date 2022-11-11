class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    result = []
    cur = head
    while cur is not None:
        result.append(cur.val)
        cur = cur.next

    return result


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

result = linked_list_values(a)
print(result)
assert result == ["a", "b", "c", "d"]
