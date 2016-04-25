def count(n, k):
    while n > 0:
        r = str(n).count('2')
        k += r
        n -= 1

    return k

if __name__ == '__main__':
    number = 1250000

    k = 0
    print (count(number, k))
