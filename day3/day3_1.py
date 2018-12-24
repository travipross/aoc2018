import re

# read data
with open("data3.txt") as f:
    data = f.read().strip()
    
# parse data
cuts = re.findall('#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', data)
for idx, op in enumerate(cuts):
    cuts[idx] = list(map(lambda x: int(x), op))

for c in cuts:
    print(c)