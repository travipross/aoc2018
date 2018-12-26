from collections import defaultdict, Counter

# read data into list of tuples
coords = []
with open('data6.txt') as f:
    for line in f.readlines():
        coords.append(tuple(map(lambda l: int(l), line.strip().split(', '))))


# helper function for computing distance
def manhattan_dist(c1, c2):
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])

# helper function for finding closest coordinate. returns idx or None if tied
def find_closest_coord(pt, coords):
    duplicate_found = False
    d_min = 1e9
    for idx, c in enumerate(coords):
        d = manhattan_dist(pt, c)
        if d < d_min:
            d_min = d
            idx_min = idx
            duplicate_found = False
        elif d == d_min:
            duplicate_found = True

    return idx_min if not duplicate_found else 'tied'


row_coords = [c[0] for c in coords]
col_coords = [c[1] for c in coords]

# get bounding box of original coords
# [min_row, max_row, min_col, max_col]
inner_limits = [min(row_coords), max(row_coords), min(col_coords), max(col_coords)]

inner_width = inner_limits[1] - inner_limits[0]
inner_height = inner_limits[3] - inner_limits[2]

# get bounding box of outer coords
outer_limits = [inner_limits[0]-int(inner_height/2), inner_limits[1]+int(inner_height/2),
                inner_limits[2]-int(inner_width/2), inner_limits[3]+int(inner_width/2)]

# loop around perimeter of outer box to get list of validation coords
inf_validation_coords = []
# top row
for c in range(outer_limits[2], outer_limits[3]+1):
    inf_validation_coords.append((outer_limits[0], c))
# bottom row
for c in range(outer_limits[2], outer_limits[3]+1):
    inf_validation_coords.append((outer_limits[1], c))
# left col
for r in range(outer_limits[0], outer_limits[1]+1):
    inf_validation_coords.append((outer_limits[2], r))
# right col
for r in range(outer_limits[0], outer_limits[1]+1):
    inf_validation_coords.append((outer_limits[3], r))

# any coordinate that is the closest to a perimeter point can't be valid
inf_coords = set()
for pt in inf_validation_coords:
    d_min = 1e9
    c_min = tuple()
    for c in coords:
        d = manhattan_dist(pt, c)
        if d < d_min:
            d_min = d
            c_min = c
    inf_coords.add(c_min)

# iterate over inner box counting how many spaces belong to coord
areas = defaultdict(int)

for r in range(inner_limits[0], inner_limits[1]+1):
    for c in range(inner_limits[2], inner_limits[3]+1):
        idx = find_closest_coord((r, c), coords)
        areas[idx] += 1

ctr = Counter(areas)

for idx, ct in ctr.most_common():
    loneliest_coord = coords[idx]
    if loneliest_coord not in inf_coords:
        break

print(loneliest_coord)
print(ct)