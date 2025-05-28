'''
This is a multi-line string literal, not a comment.
'''
print('Hello Python World!')

# those are some variables
myStart = 5
myEnd = 18

# here's an example of interpolated string and loop
print(f'Looping in interval [{myStart}, {myEnd}]')

# enumerate() returns a tuple with the index and the value from the iteratable at that index
for idx, n in enumerate(range(myStart, myEnd+1)):
    print(f'n[{idx}] = {n}')

