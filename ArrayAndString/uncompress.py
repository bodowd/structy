## my implementation

# def uncompress(input):
#     i = 0
#     result = ""
#     while i <= len(input) - 1:
#         number = ""
#         while not input[i].isalpha() and i <= len(input) - 1:
#             number += input[i]
#             i += 1

#         if number != "":
#             int_number = int(number)
#         result += int_number * input[i]
#         i += 1

#     return result

## structy implementation
def uncompress(s):
    # Two pointers -- one pointer moves forward to find all the numbers, the slower pointer marks the beginning of the number
    # and the faster pointer marks the end of the number

    numbers = "0123456789"
    result = []
    j = 0
    i = 0

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j
    return "".join(result)


result = uncompress("2c3a1t")
print(result)
assert result == "ccaaat"

result = uncompress("4s2b")
print(result)
assert result == "ssssbb"

result = uncompress("2p1o5p")
print(result)
assert result == "ppoppppp"

result = uncompress("3n12e2z")
print(result)
assert result == "nnneeeeeeeeeeeezz"

result = uncompress("127y")
print(result)
assert (
    result
    == "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
)
