from collections import Counter

path = "data2.txt"

with open(path) as f:
    data = f.read().strip().splitlines()

for idx in range(len(data)):
    boxes = data.copy()
    a1 = boxes.pop(idx)
    for a2 in boxes:
        # count different chars
        diffct = 0
        diffpos = []
        for pos, char in enumerate(a2):
            if a1[pos] != char:
                diffct += 1
                diffpos.append(pos)
        if diffct == 1:
            print("Found 1")
            # if exactly 1 different char, check no more
            break
    if diffct == 1:
        break

def remove_idx_from_string(s, idx):
    return s[:idx] + s[idx+1:]

# print results
print(a1)
print(a2)
print(diffpos)

s = a1
for x in range(len(diffpos)):
    s = remove_idx_from_string(s, diffpos.pop())


print(s)