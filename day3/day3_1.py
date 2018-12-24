import re
import numpy as np

# read data
with open("data3.txt") as f:
    data = f.read().strip()
    
# parse data
cuts = re.findall('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', data)
for idx, op in enumerate(cuts):
    cuts[idx] = list(map(lambda x: int(x), op))

# initialize array
arr = np.zeros([1000,1000], dtype=int)

# add cuts
def update_cuts(a, cut_list):
    col_start = cut_list[1]
    row_start = cut_list[2]
    col_size = cut_list[3]
    row_size = cut_list[4]
    col_end = col_start+col_size
    row_end = row_start+row_size
    
    a[row_start:row_end, col_start:col_end] += np.ones([row_size, col_size], dtype=int)
    return a

for c in cuts:
    arr = update_cuts(arr, c)

# count overlapping areas (non-zero)
num_overlap = (arr > 1).nonzero()[0].shape[0]
print("Overlapping segments: %d" % num_overlap)

#################### part 2 ########################

# if cut doesn't overlap any other, all indeces should be 1 for that slice
def check_array_slice(a, cut_list):
    col_start = cut_list[1]
    row_start = cut_list[2]
    col_size = cut_list[3]
    row_size = cut_list[4]
    col_end = col_start+col_size
    row_end = row_start+row_size
    
    return np.array_equal(a[row_start:row_end, col_start:col_end], np.ones([row_size, col_size], dtype=int))

for c in cuts:
    if check_array_slice(arr, c):
        print("Index %d doesn't overlap with any other" % c[0])
        break