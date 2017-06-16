import time, timeit

start_time = time.time()

def minimum_adjustments(mesaj, versions, m, n, nr_var):
    dp = [[None for i in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            found_similar = False
            for k in range(int(nr_var)):
                if mesaj[i - 1] == versions[k][j - 1]:
                    found_similar = True
                    break
            if found_similar:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]

if __name__ == '__main__':
    file_input = open('evaluare.in', 'r')
    file_output = open('evaluare.out', 'w')

    strings = file_input.read().split("\n")

    [NR_VAR, N] = map(int, strings[0].split())

    versions = []
    for i in range(1, NR_VAR + 1):
        versions.append(map(int, strings[i].split()))

    M = int(strings[NR_VAR + 1])
    mesaj = strings[NR_VAR + 2].split()

    file_output.write(str(minimum_adjustments(mesaj, versions, M, N, NR_VAR)))

    file_input.close()
    file_output.close()
print("--- %s seconds ---" % (time.time() - start_time))
