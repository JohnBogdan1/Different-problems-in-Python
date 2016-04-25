global set_str
set_str = []


def func(old, new):
    if len(old) == 0:
        set_str.append(new)
        return
    if len(old) > 1:
        repeat_time = 2
    else:
        repeat_time = 1

    for i in range(repeat_time):
        key = old[:i + 1]
        if key > 'z':
            return
        func(old[i + 1:], new + str(unichr(int(key) + 96)))


if __name__ == '__main__':
    number = "11223"
    func(number, "")
    for c in set_str:
        print c
