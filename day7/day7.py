import re
from itertools import chain
from collections import defaultdict

# read file
with open('data7_test.txt') as f:
    raw = f.read()

# parse the data
pattern = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin.\n?'
steps = re.findall(pattern, raw)

# build data structure to indicate prerequisites
pr = defaultdict(list)
for step in steps:
    pr[step[1]].append(step[0])


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


# while any pre-requisites exist, continue performing steps
steps_performed = ''
while pr:
    # any item in set of prerequisites that's not in set of keys is ready to be done
    s_keys = set(pr.keys())
    s_vals = set(chain.from_iterable(pr.values()))
    prs_ready_to_be_done = sorted(list(set.difference(s_vals, s_keys)))

    # determine what step to do next
    if not prs_ready_to_be_done:
        raise IndexError('No possible steps remain')
    else:
        step_to_do = sorted(prs_ready_to_be_done)[0]

    perform_step(step_to_do, pr)
    steps_performed += step_to_do
    # print("Performed step %s" % step_to_do)

# the last item in keys is the last step to perform
steps_performed += s_keys.pop()
print(steps_performed)

# not BOJYAKESNGTWMXFZQVRDHIULP
# answer JNOIKSYABEQRUVWXGTZFDMHLPC


########### part 2 ##################
n_workers = 2
bias = ord('A') - 1
times = [ord(x)-bias for x in steps_performed]

step_times = dict(zip(steps_performed, times))
remaining_steps = list(steps_performed)
workers = [0]*n_workers
elapsed = 0
while True:
    # if steps left, try to assign to any available workers ( no time)
    if remaining_steps:
        for idx, w in enumerate(workers):
            if w == 0 and remaining_steps:
                workers[idx] = step_times.get(remaining_steps.pop(0))
                continue

    else:
        if not any(workers):
            break
    elapsed += 1
    workers = [w-1 if w > 0 else 0 for w in workers]

print(elapsed)