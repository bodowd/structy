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


def remove_node(head, target_val):
    if head.val == target_val:
        return head.next
    prev = None
    cur = head
    while cur is not None:
        if cur.val == target_val:
            prev.next = cur.next
            # remove only the first occurrence of a duplicate value
            break
        prev = cur
        cur = cur.next
    return head


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

# a -> b -> c -> d -> e -> f

result = print_list(remove_node(a, "c"))
print(result)
assert result == ["a", "b", "d", "e", "f"]
# a -> b -> d -> e -> f

x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z

# x -> y -> z

result = print_list(remove_node(x, "z"))
print(result)
assert result == ["x", "y"]
# x -> y


q = Node("q")
r = Node("r")
s = Node("s")

q.next = r
r.next = s

# q -> r -> s

result = print_list(remove_node(q, "q"))
print(result)
assert result == ["r", "s"]
# r -> s

node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")

node1.next = node2
node2.next = node3
node3.next = node4

# h -> i -> j -> i

result = print_list(remove_node(node1, "i"))
print(result)
assert result == ["h", "j", "i"]
# h -> j -> i

t = Node("t")

# t

result = print_list(remove_node(t, "t"))
print(result)
assert result == []
# None
