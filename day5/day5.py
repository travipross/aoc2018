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

# convert to list
l = [c for c in s]
n = 0
while True:
    # count polymer reactions in pass. Once none are destroyed in a pass, finish
    poly_destroyed = False
    for idx in range(len(l)-1):
        c1 = l[idx]
        c2 = l[idx+1]
        if is_opposite_case(c1, c2):
            #print("c1 = %s, c2 = %s, deleting %s" % (c1, c2, l[idx:idx+2]))
            del l[idx:idx+2]
            poly_destroyed = True
            break
        
    if poly_destroyed:
        continue

s_reduced = str.join('',l)
print(s_reduced)
