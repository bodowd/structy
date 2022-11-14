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


def zipper(head1, head2):
    tail = head1
    p1 = head1.next
    p2 = head2
    count = 0
    while p1 is not None and p2 is not None:
        # if count is even, take from list 2, else take from list 1
        if count % 2 == 0:
            tail.next = p2
            # advance p2
            p2 = p2.next
        else:
            tail.next = p1
            p1 = p1.next
        tail = tail.next
        count += 1

    if p1 is None:
        tail.next = p2
    if p2 is None:
        tail.next = p1

    return head1


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

result = print_list(zipper(a, x))
print(result)
assert result == ["a", "x", "b", "y", "c", "z"]

w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3

result = print_list(zipper(w, one))
print(result)
assert result == ["w", 1, 2, 3]
