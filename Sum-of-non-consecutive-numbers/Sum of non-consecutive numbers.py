def suma(v):
    length = len(v)
    curr = v[0]
    excurr = 0

    for i in range(1, length):
        if curr > excurr:
            newcurr = curr
        else:
            newcurr = excurr

        curr = excurr + v[i]
        excurr = newcurr

    max = 0

    if curr > excurr:
        max = curr
    else:
        max = excurr
    return max


def rec_sum(n):
    if n == 0:
        return v[0]
    elif n == 1:
        return max(v[0], v[1])
    else:
        return max(rec_sum(n - 2) + v[n], rec_sum(n - 1))


if __name__ == '__main__':
    v = [16, 15, 3, 4, 12, 4]
    print suma(v)
    print rec_sum(len(v) - 1)
