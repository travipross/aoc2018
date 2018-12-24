filename = 'data1.txt'

with open(filename) as f:
    data = f.read().split('\n')
    
total = 0
for x in data:
    if x.startswith('+'):
        total += int(x.split('+')[1])
    elif x.startswith('-'):
        total -= int(x.split('-')[1])
    else:
        raise ValueError('No mathematical operator found on line: %s' % x)

print("Total = %d" % total)
