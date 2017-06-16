if __name__ == '__main__':

    input = open("date.in", "r")

    [nr_pairs, total_weight] = map(int, input.readline().split())

    weights = []
    values = []

    for i in xrange(nr_pairs):
        [weight, value] = map(int, input.readline().split())

        weights.append(weight)
        values.append(value)
        print weight, value

    matrix = [[0 for i in xrange(total_weight + 1)] for j in xrange(nr_pairs)]

    for i in xrange(nr_pairs):
        for j in xrange(total_weight + 1):
            if weights[i] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weights[i]] + values[i])

    """for line in matrix:
        print line"""

    print "MAX:", matrix[nr_pairs - 1][total_weight]
