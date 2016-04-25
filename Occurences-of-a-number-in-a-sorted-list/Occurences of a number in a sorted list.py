def count(v, x, n):
    i = first(v, x, 0, n - 1, n)

    if i == -1:
        return i

    j = last(v, x, i, n - 1, n)

    return j - i + 1


def first(v, x, start, end, n):
    if start > end:
        return -1

    mid = (start + end) / 2

    if (mid == 0 or x > v[mid - 1]) and v[mid] == x:
        return mid
    elif v[mid] < x:
        return first(v, x, mid + 1, end, n)
    else:
        return first(v, x, start, mid - 1, n)


def last(v, x, start, end, n):
    if start > end:
        return -1

    mid = (start + end) / 2

    if (mid == n - 1 or x < v[mid + 1]) and v[mid] == x:
        return mid
    elif v[mid] > x:
        return last(v, x, start, mid - 1, n)
    else:
        return last(v, x, mid + 1, end, n)


if __name__ == '__main__':
    v = [2, 2, 4, 4, 10, 10, 20, 35, 35, 39]
    x = 39
    print count(v, x, len(v))
