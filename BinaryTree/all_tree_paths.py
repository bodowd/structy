class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None


def all_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []
    left_paths = all_tree_paths(root.left)
    right_paths = all_tree_paths(root.right)

    for path in left_paths:
        paths.append([root.val, *path])

    for path in right_paths:
        paths.append([root.val, *path])
    return paths


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

r = all_tree_paths(a)
print(r)
assert r == [["a", "b", "d"], ["a", "b", "e"], ["a", "c", "f"]]

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i

r = all_tree_paths(a)
print(r)
assert r == [
    ["a", "b", "d"],
    ["a", "b", "e", "g"],
    ["a", "b", "e", "h"],
    ["a", "c", "f", "i"],
]
