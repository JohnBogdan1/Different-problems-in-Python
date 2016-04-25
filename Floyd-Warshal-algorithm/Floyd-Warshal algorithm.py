def floyd_warshal(costs, next):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (costs[i][k] + costs[k][j] < costs[i][j]):
                    costs[i][j] = costs[i][k] + costs[k][j]
                    next[i][j] = next[i][k]

    return (costs, next)


def reconstruct_path(next, start, end):
    if next[start][end] == -1:
        return []

    path = [start]
    while start != end:
        start = next[start][end]
        path.append(start)

    return path


if __name__ == '__main__':
    input = open("floyd.in", "r")

    [N, M] = map(int, input.readline().split())
    costs = [[99999 for i in range(N)] for i in range(N)]
    next = [[-1 for i in range(N)] for i in range(N)]

    for i in range(M):
        [j, k, cost] = map(int, input.readline().split())
        next[j][k] = k
        costs[j][k] = cost

    # print(costs)
    print()
    start = 0
    end = 5
    print(floyd_warshal(costs, next))

    print(reconstruct_path(next, start, end))
