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


def merge_lists(head_1, head_2):
    # use dummy instead of tail that way we can always make p1 head_1 and p2 head_2. Otherwise, you have to
    # figure out which p1 should be depending on if you make tail = head_1 or head_2 (tail = head_1 if head_1 < head_2)

    # remember the new head of the merged lists
    dummy = Node(0)
    prev = dummy
    p1 = head_1
    p2 = head_2

    while p1 is not None and p2 is not None:
        if p2.val < p1.val:
            prev.next = p2
            p2 = p2.next
        else:
            prev.next = p1
            p1 = p1.next
        prev = prev.next

    if p1 is None:
        prev.next = p2
    if p2 is None:
        prev.next = p1

    return dummy.next


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

result = print_list(merge_lists(a, q))
print(result)
assert result == [5, 6, 7, 8, 9, 10, 12, 20, 25, 28]


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(1)
r = Node(8)
s = Node(9)
t = Node(10)
q.next = r
r.next = s
s.next = t
# 1 -> 8 -> 9 -> 10

result = print_list(merge_lists(a, q))
print(result)
assert result == [1, 5, 7, 8, 9, 10, 10, 12, 20, 28]
