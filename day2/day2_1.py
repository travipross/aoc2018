from collections import Counter

path = "data2.txt"

with open(path) as f:
    data = f.read().strip().splitlines()
print("%d boxes.." % len(data))
twos = 0
threes = 0
for d in data:
    c = Counter(d)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1

chk = twos*threes

print("Two common letters: %d" % twos)
print("Three common letters: %d" % threes)
print("Checksum: %d" % chk)

# not 25245