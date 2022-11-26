import sys

sys.setrecursionlimit(200000)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_finder(root, target):
    result = _path_finder(root, target)
    if result is None:
        return None
    return result[::-1]


def _path_finder(root, target):
    # only if the target is found is a populated list bubbled up. otherwise it's just None that is bubbled up
    if root is None:
        return None
    if root.val == target:
        return [root.val]

    left_path = _path_finder(root.left, target)
    right_path = _path_finder(root.right, target)

    if left_path is not None:
        left_path.append(root.val)
        return left_path
    # return [root.val, *left_path]

    if right_path is not None:
        right_path.append(root.val)
        return right_path
    # return [root.val, *right_path]

    return None


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

r = path_finder(a, "e")
print(r)
assert r == ["a", "b", "e"]

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

r = path_finder(a, "p")
print(r)
assert r == None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

r = path_finder(a, "c")
print(r)
assert r == ["a", "c"]

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

r = path_finder(a, "h")
print(r)
assert r == ["a", "c", "f", "h"]

x = Node("x")

#      x

r = path_finder(x, "x")
print(r)
assert r == ["x"]

r = path_finder(None, "x")
print(r)
assert r == None

root = Node(0)
curr = root
for i in range(1, 19500):
    curr.right = Node(i)
    curr = curr.right

#      0
#       \
#        1
#         \
#          2
#           \
#            3
#             .
#              .
#               .
#              19498
#                \
#                19499

r = path_finder(root, 16281)
assert r == list(range(0, 16282))
# [0, 1, 2, 3, ..., 16280, 16281]
