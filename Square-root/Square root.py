import math


def square_root(val):
    low = 0
    high = mid = val
    oldmid = -1

    while math.fabs(oldmid - mid) >= 0.001:

        oldmid = mid

        mid = float((low + high) / 2)

        mid_square = mid * mid

        if mid_square > val:
            high = mid
        else:
            low = mid
    return [val, mid]


if __name__ == '__main__':
    print square_root(3)
