import heapq
from collections import deque


def dijkstra(pairs, distances, nodes, sursa, destinatie):
    Q = []
    selected = {}
    parent = {}
    dist_values = {}

    for nod in nodes:
        selected[nod] = False

    selected[sursa] = True

    for nod in nodes:
        if nod in pairs[sursa]:
            dist_values[nod] = distances[(sursa, nod)]
            heapq.heappush(Q, nod)
            parent[nod] = sursa
        else:
            dist_values[nod] = float("inf")
            parent[nod] = None

    while len(Q) != 0:
        u = heapq.heappop(Q)
        selected[u] = True
        for nod in pairs[u]:
            if (not selected[nod]) and dist_values[nod] > dist_values[u] + distances[(u, nod)]:
                dist_values[nod] = dist_values[u] + distances[(u, nod)]
                parent[nod] = u
                heapq.heapify(Q)

    # o coada(double-ended queue), pentru a insera la inceput
    drum = deque()
    nod = parent[destinatie]

    while nod != None:
        drum.appendleft(nod)
        nod = parent[nod]

    # adaug si destinatia
    drum.append(destinatie)

    # returnez drumul
    return "Drum intre %s si %s: %s" % (sursa, destinatie, list(drum))


if __name__ == '__main__':
    input = open("dijkstra.in", "r")
    N = int(input.readline())
    nodes = []
    for i in range(N):
        # rstrip removes newlines
        nodes.append(input.readline().rstrip())

    M = int(input.readline())
    pairs = {}
    distances = {}
    for i in range(M):
        [x, y, cost] = input.readline().split()
        pairs.setdefault(x, list()).append(y)
        pairs.setdefault(y, list()).append(x)
        distances[(x, y)] = int(cost)
        distances[(y, x)] = int(cost)

    print("PAIRS: ", pairs)
    print()

    print("DISTANCES: ", distances)
    print()

    print("NODES: ", nodes)
    print()

    sursa = "Bucuresti"

    for destinatie in nodes:
        print(dijkstra(pairs, distances, nodes, sursa, destinatie))
