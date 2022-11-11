from webbrowser import get


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_node_value(head, index):
    cur_index = 0
    cur = head

    while cur is not None:
        if cur_index == index:
            return cur.val

        cur_index += 1
        cur = cur.next
    return None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

res = get_node_value(a, 2)
print(res)
assert res == "c"

res = get_node_value(a, 7)
print(res)
assert res == None
