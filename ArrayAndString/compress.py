def compress(s):
    s += "!"  # need a dummy character at the end of the string or else you get out of index error on the last letter s[j]
    result = []
    i, j = 0, 0

    while j < len(s):
        # expand the window while the letters are the same
        if s[i] == s[j]:
            j += 1
        else:
            letter = s[i]
            num = j - i

            if num == 1:
                result.append(letter)
            else:
                result.append(str(num))
                result.append(letter)
            i = j
    return "".join(result)


result = compress("ccaaatsss")
print(result)
assert result == "2c3at3s"

result = compress("ssssbbz")
print(result)
assert result == "4s2bz"

result = compress("ppoppppp")
print(result)
assert result == "2po5p"

result = compress("nnneeeeeeeeeeeezz")
print(result)
assert result == "3n12e2z"

result = compress(
    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
)
print(result)
assert result == "127y"
