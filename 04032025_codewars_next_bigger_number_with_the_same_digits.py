def next_bigger(n):
    s = list(str(n))
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i == -1:
        return -1
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = sorted(s[i + 1:])
    try:
        result = int("".join(s))
    except ValueError:
        return -1
    if result == n:
        return -1

    return result