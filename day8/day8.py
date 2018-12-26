with open('data8.txt') as f:
    data = [int(x) for x in f.read().split()]

#data = [int(x) for x in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()]

# use recursion to parse indefinitely


def parse(data):
    # extract header
    children, metas = data[:2]
    data = data[2:]

    # recursively add totals from child nodes
    totals = 0
    for i in range(children):
        # recursive step
        total, data = parse(data)
        totals += total

    # add totals from current node
    totals += sum(data[:metas])

    return totals, data[metas:]


print(parse(data)[0])