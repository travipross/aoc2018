filename = 'data1_test3.txt'

with open(filename) as f:
    data = f.read().split('\n')

list_of_totals = []
total = 0
l = len(data)
idx = 0

# loop indefinitely and rely on break statement for exit
while True:
    # read and add/subtract data
    x = data[idx]    
    if x.startswith('+'):
        total += int(x.split('+')[1])
    elif x.startswith('-'):
        total -= int(x.split('-')[1])
    else:
        raise ValueError('No mathematical operator found on line: %s' % x)
    
    # check exit condition
    if total in list_of_totals:
        break
        
    # append current frequency to list
    list_of_totals.append(total)
    
    # loop around if at the end of the list of frequency shifts  
    idx += 1
    if idx >= l:
        print("Loop reset.. %d items in list" % len(list_of_totals))
        idx = 0
    
print("Frequency changes: %d" % len(list_of_totals))
print("First repeating frequency: %s" % total)

