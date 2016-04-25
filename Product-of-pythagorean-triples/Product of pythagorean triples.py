def find_triples(n):
    for i in range(n / 3):
        for j in range(i + 1, n / 2):
            k = n - i - j
            if i + j + k == n and i ** 2 + j ** 2 == k ** 2:
                return i, j, k


if __name__ == '__main__':
    list = find_triples(int(raw_input()))
    print list
    product = 1
    for nr in list:
        product *= nr
    print product
