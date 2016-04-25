def tree(n):
    christmas_tree = []
    nr = n
    k = 1
    for i in range(n):
        christmas_tree.append(nr * "." + k * "*" + nr * ".")
        nr -= 1
        k += 2
    christmas_tree.append(n * "." + "*" + n * ".")

    return christmas_tree


if __name__ == '__main__':
    n = int(raw_input())
    for row in tree(n):
        print row
