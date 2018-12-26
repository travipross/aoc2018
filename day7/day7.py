import re
from collections import defaultdict

# read file
with open('data7.txt') as f:
    raw = f.read()

# parse the data
pattern = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin.\n?'
steps = re.findall(pattern, raw)

# build data structure to indicate prerequisites
pr = defaultdict(list)
for step in steps:
    before = step[0]
    after = step[1]
    pr[after].append(before)


# create helper function to remove items from prerequisites
def perform_step(s, pr):
    keys_to_delete = []
    for k, v in pr.items():
        pr[k] = [i for i in v if i != s] # remove item from list
        # if list is empty, delete key from dict
        if not pr[k]:
            keys_to_delete.append(k)

    for key in keys_to_delete:
        del pr[key]


# look for any step having only one pre-requisite
steps_performed = ''
while pr:
    possible_steps = [p[0] for p in pr.values() if len(p) == 1]
    # if no possible steps are found, there must be an error
    if not possible_steps:
        raise IndexError('No possible steps remain')

    step_to_do = sorted(possible_steps)[0]
    steps_performed += step_to_do
    perform_step(step_to_do, pr)

print(steps_performed)



