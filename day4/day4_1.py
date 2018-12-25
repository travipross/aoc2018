import re
from collections import defaultdict, Counter

rawdata = sorted(open('data4.txt').read().splitlines())

#groups = re.findall('\[[0-9]{4}-([0-9]{2})-([0-9]{2}) [0-9]{2}\:([0-9][0-9])\] (.+)\n?', rawdata)
all_mins = list(range(60))

# sorted in order. Always starts shift before sleep or wake
guards = defaultdict(list)
times = defaultdict(int)
for event in rawdata:
    
    # 3 cases: guard #x starts shift, falls asleep, wakes up
    if "begins shift" in event:
        id = int(event.split('#')[1].split()[0])
    elif "falls asleep" in event:
        start = int(event.split('] ')[0][-2:])
    elif "wakes up" in event:
        stop = int(event.split('] ')[0][-2:])
        for x in range(start, stop):
            guards[id].append(x)
            times[id] += (stop-start)

# find guard that was asleep the most
max_guard, max_time = max(times.items(), key=lambda i: i[1])


# find minute the guard was asleep the most
max_minute, count = Counter(guards[max_guard]).most_common(1)[0]

ans = max_guard*max_minute
print(ans)


############ part 2 ##############
max_count = -1
guard_id = -1
for g in guards: # counts by key
    max_minute, count = Counter(guards[g]).most_common(1)[0]
    if count > max_count:
        guard_id = g
        max_count = count
        max_minute_overall = max_minute

print(guard_id*max_minute_overall)