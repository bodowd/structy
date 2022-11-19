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


def insert_node(head, node_val, index):
    new_node = Node(node_val)

    cur = head

    if index == 0:
        new_node.next = cur
        return new_node

    count = 0

    while cur is not None:

        if index - 1 == count:
            temp = cur.next
            cur.next = new_node
            new_node.next = temp
        cur = cur.next
        count += 1

    return head


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

result = print_list(insert_node(a, "x", 2))
print(result)
assert result == ["a", "b", "x", "c", "d"]
# a -> b -> x -> c -> d

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

result = print_list(insert_node(a, "v", 3))
print(result)
assert result == ["a", "b", "c", "v", "d"]
# a -> b -> c -> v -> d

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

result = print_list(insert_node(a, "m", 4))
print(result)
assert result == ["a", "b", "c", "d", "m"]
# a -> b -> c -> d -> m

a = Node("a")
b = Node("b")

a.next = b

# a -> b

result = print_list(insert_node(a, "z", 0))
print(result)
assert result == ["z", "a", "b"]
# z -> a -> b
