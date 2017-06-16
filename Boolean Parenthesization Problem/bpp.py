def count_number_of_ways(operands, operators):
    n = len(operands)

    matrix_true = [[0 for i in xrange(n)] for j in xrange(n)]
    matrix_false = [[0 for i in xrange(n)] for j in xrange(n)]

    for i in xrange(n):
        matrix_true[i][i] = 1 if operands[i] == "true" else 0
        matrix_false[i][i] = 1 if operands[i] == "false" else 0

    for l in xrange(2, n + 1):
        for i in xrange(n + 1 - l):
            j = i + l - 1
            for k in xrange(i, j):

                if operators[k] == "and":
                    matrix_true[i][j] += matrix_true[i][k] * matrix_true[k + 1][j]
                    matrix_false[i][j] += matrix_true[i][k] * matrix_false[k + 1][j] + matrix_false[i][k] * \
                                                                                       matrix_true[k + 1][j] + \
                                          matrix_false[i][k] * matrix_false[k + 1][j]

                if operators[k] == "or":
                    matrix_false[i][j] += matrix_false[i][k] * matrix_false[k + 1][j]
                    matrix_true[i][j] += matrix_true[i][k] * matrix_false[k + 1][j] + matrix_false[i][k] * \
                                                                                      matrix_true[k + 1][j] + \
                                         matrix_true[i][k] * matrix_true[k + 1][j]

                if operators[k] == "xor":
                    matrix_true[i][j] += matrix_true[i][k] * matrix_false[k + 1][j] + matrix_false[i][k] * \
                                                                                      matrix_true[k + 1][j]
                    matrix_false[i][j] += matrix_true[i][k] * matrix_true[k + 1][j] + matrix_false[i][k] * \
                                                                                      matrix_false[k + 1][j]

    return matrix_true[0][n - 1]


if __name__ == '__main__':
    expression = "true or true and false xor true"

    splitExpression = expression.split(" ")

    operands = [splitExpression[i] for i in xrange(len(splitExpression)) if i % 2 == 0]
    operators = [splitExpression[i] for i in xrange(len(splitExpression)) if i % 2 != 0]

    print operators, operands

    print "Number of ways:", count_number_of_ways(operands, operators), "ways"
