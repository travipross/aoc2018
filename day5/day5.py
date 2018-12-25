with open('data5.txt') as f:
    s = f.read()

# define helper functions
def is_lower(a):
    return a == a.lower()

def is_upper(a):
    return a == a.upper()

def is_opposite_case(a1, a2):
    if (a1.lower() != a2.lower()):
        return False
    else:
        return (is_lower(a1) and is_upper(a2)) or (is_upper(a1) and is_lower(a2))

def delete_idxs_from_list(l, idxs):
    for idx in sorted(idxs, reverse=True):
        del l[idx]
    return l

# convert to list
l = [c for c in s]

# loop over list, checking pairs
idxs_to_delete = []
idx = 0
while idx < len(l)-1:
    # mark indeces of pair matches
    c1 = l[idx]
    c2 = l[idx+1]
    if is_opposite_case(c1, c2):
        # print("%d) c1 = %s, c2 = %s, deleting %s" % (idx, c1, c2, l[idx:idx+2]))
        idxs_to_delete.extend([idx, idx+1])
        idx += 2
    else:
        idx += 1

l = delete_idxs_from_list(l, idxs_to_delete)

s_reduced = str.join('',l)
print(s_reduced)
