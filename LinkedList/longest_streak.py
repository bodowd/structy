class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# # my solution
# def longest_streak(head):
#     max_count = 1
#     current_count = 1
#     if head is None:
#         return 0
#     prev = head
#     cur = head.next
#     while cur is not None:
#         if prev.val == cur.val:
#             current_count += 1
#         if max_count < current_count:
#             max_count = current_count
#             current_count = 1
#         prev = cur
#         cur = cur.next

#     return max_count


# structy solution is nicer i think
def longest_streak(head):
    if head is None:
        return 0
    streak = 0
    streak_val = head.val
    cur = head
    max_streak = 0

    while cur is not None:
        if streak_val == cur.val:
            streak += 1
        else:
            max_streak = max(max_streak, streak)
            streak = 1
            streak_val = cur.val
        cur = cur.next

    return max(max_streak, streak)


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

result = longest_streak(a)  # 3
print(result)
assert result == 3


a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9
result = longest_streak(a)  # 3
print(result)
assert result == 3

a = Node(5)
b = Node(5)

a.next = b

# 5 -> 5

result = longest_streak(a)  # 2
print(result)
assert result == 2


a = Node(4)

# 4

result = longest_streak(a)  # 1
print(result)
assert result == 1


result = longest_streak(None)
print(result)
assert result == 0
