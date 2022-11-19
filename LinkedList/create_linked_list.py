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


# my implementation
def create_ll(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = Node(arr[i])
        cur = cur.next

    return head


ll = create_ll(["h", "e", "y"])
result = print_list(ll)
print(result)
assert result == ["h", "e", "y"]

ll = create_ll([1, 7, 1, 8])
result = print_list(ll)
print(result)
assert result == [1, 7, 1, 8]


ll = create_ll(["a"])
result = print_list(ll)
print(result)
assert result == ["a"]

ll = create_ll([])
result = print_list(ll)
print(result)
assert result == []
