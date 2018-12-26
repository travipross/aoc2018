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
    values = []
    for i in range(children):
        # recursive step
        total, data, value = parse(data)
        totals += total
        values.append(value) # values is a list of child values

    # add totals from current node
    totals += sum(data[:metas])
    if children == 0:
        out_value = sum(data[:metas])
    else:
        out_value = sum(values[k-1] for k in data[:metas] if 0 < k <= len(values))

    return totals, data[metas:], out_value


print(parse(data))