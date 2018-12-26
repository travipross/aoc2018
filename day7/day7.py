import re
import copy
from itertools import chain
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
    pr[step[1]].append(step[0])
pr_copy = copy.deepcopy(pr)

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
step_order = ''
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
    step_order += step_to_do
    # print("Performed step %s" % step_to_do)

# the last item in keys is the last step to perform
step_order += s_keys.pop()
print(step_order)

# not BOJYAKESNGTWMXFZQVRDHIULP
# answer JNOIKSYABEQRUVWXGTZFDMHLPC


########### part 2 ##################
n_workers = 5

backlog = list(step_order)
in_progress = dict()
complete = set()

bias = ord('A') - 61
times = dict(zip(backlog, [ord(x)-bias for x in step_order]))


def prerequisites_complete(step, pr, done):
    return set(pr.get(step, [])).issubset(set(done))

elapsed = 0
while len(backlog) or len(in_progress):
    # for every step that's ready to be done, begin action
    if len(in_progress) < n_workers:
        for idx, s in enumerate(backlog):
            if prerequisites_complete(s, pr_copy, complete):
                in_progress.update({s: times[s]})
                del backlog[idx]
    print(elapsed, in_progress)
    # for every item in progress, update time (and complete if necessary)
    keys_to_delete = []
    for k,v in in_progress.items():
        in_progress[k] = v - 1
        if in_progress[k] == 0:
            complete.add(k)
            keys_to_delete.append(k)
    for k in keys_to_delete:
        del in_progress[k]
    elapsed += 1


print(elapsed)

