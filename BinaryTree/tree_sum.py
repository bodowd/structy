class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    if root is None:
        return 0

    left_vals = tree_sum(root.left)
    right_vals = tree_sum(root.right)

    return root.val + left_vals + right_vals


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

result = tree_sum(a)
print(result)
assert result == 21

a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

result = tree_sum(a)
print(result)
assert result == 10

result = tree_sum(None)
print(result)
assert result == 0
