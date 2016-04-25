def LCM_2order(a, b):
    p = a * b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return p / a


def LCM(list):
    if len(list) == 2:
        return LCM_2order(list[0], list[1])
    else:
        return LCM_2order(list[0], LCM(list[1:]))


if __name__ == '__main__':
    list = map(int, raw_input().split())
    # LCM(a,b,c) = LCM(a,LCM(b,c))
    # list : 1 2 3 4
    print LCM(list)
