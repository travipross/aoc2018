from itertools import cycle

filename = 'data1.txt'

with open(filename) as f:
    data = f.read().split('\n')

list_of_totals = {0}
total = 0
l = len(data)
idx = 0

def performStringOperation(tot, op):
    if op.startswith('+'):
        tot += int(op.split('+')[1])
    elif op.startswith('-'):
        tot -= int(op.split('-')[1])
    else:
        raise ValueError('No mathematical operator found on line: %s' % op)
    return tot

# get list of totals for one full iteration 
for x in cycle(data):
    total = performStringOperation(total, x)
    if total in list_of_totals:
        break
    list_of_totals.add(total)


########## DUMB WAY TO DO IT ###########
# # loop indefinitely and rely on break statement for exit
# while True:
#     # read and add/subtract data
#     total = performStringOperation(total, data[idx])
#     
#     # check exit condition
#     if total in list_of_totals:
#         break
#         
#     # append current frequency to list
#     list_of_totals.append(total)
#     
#     # loop around if at the end of the list of frequency shifts  
#     idx += 1
#     if idx >= l:
#         print("Loop reset.. %d items in list" % len(list_of_totals))
#         idx = 0
#     
# print("Frequency changes: %d" % len(list_of_totals))
print("First repeating frequency: %s" % total)

