if __name__ == '__main__':

    input = open("date1.in", "r")

    pairs = []
    nr_homeworks = int(input.readline())

    for i in xrange(nr_homeworks):
        [deadline, value] = map(int, input.readline().split())
        pairs.append([value, deadline])

    # sort after value in decreasing order
    sorted_pairs = sorted(pairs, reverse=True)

    # 2 vectors, one for checking the available slot, another for putting the result
    no_planned = [False for i in range(nr_homeworks)]
    result = [0 for i in range(nr_homeworks)]

    i = 0
    for pair in sorted_pairs:
        value = pair[0]
        deadline = pair[1]

        # i check all slots in the vector starting from this index
        #
        index = min(nr_homeworks, deadline) - 1

        while index >= 0:
            if no_planned[index] == False:
                result[index] = i
                i += 1
                no_planned[index] = True
                break

            index -= 1

    sum = 0
    for i in range(nr_homeworks):
        if no_planned[i] == True:
            sum += sorted_pairs[result[i]][0]
            print "deadline %d and value %d " % (sorted_pairs[result[i]][1], sorted_pairs[result[i]][0])
    print "maximum points: %d" % (sum)
