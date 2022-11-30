class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None


def how_high(root):
    if root is None:
        return -1
    return 1 + max(how_high(root.left), how_high(root.right))


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

result = how_high(a)
print(result)
assert result == 2
