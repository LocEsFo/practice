def array_diff(a, b):
    while i < len(a):
        for j in range(len(b)):
            if a[i] == b[j]:
                a.remove(b[j])
    return a