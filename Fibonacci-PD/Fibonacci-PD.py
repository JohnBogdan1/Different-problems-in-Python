# limited DP by n
def fibo(prev_results, n):
    if n in prev_results:
        return prev_results[n]
    else:
        if n <= 2:
            f = 1
        else:
            f = fibo(prev_results, n - 1) + fibo(prev_results, n - 2)
    prev_results[n] = f
    return f


# unlimited DP
def fib(n):
    if n <= 2:
        return 1
    else:
        f1 = 1
        f2 = 1
        f = 0
        for i in xrange(2, n):
            f = f1 + f2
            f1 = f2
            f2 = f
    return f


if __name__ == '__main__':
    print fibo({}, 100)
    print fib(100)
