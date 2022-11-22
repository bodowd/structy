class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    # base case
    if root is None:
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.val, *left_values, *right_values]


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

result = depth_first_values(a)
print(result)
assert result == ["a", "b", "d", "e", "c", "f"]

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

result = depth_first_values(a)
print(result)
assert result == ["a", "b", "d", "e", "g", "c", "f"]

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

result = depth_first_values(a)
print(result)
assert result == ["a", "b", "c", "d", "e"]

result = depth_first_values(None)
print(result)
assert result == []
