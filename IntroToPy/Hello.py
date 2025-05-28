'''
This is a multi-line string literal, not a comment.
'''
print('Hello Python World!')

# those are some variables
myStart = 5
myEnd = 18

# here's an example of interpolated string and loop
print(f'\nLooping in interval [{myStart}, {myEnd}]')

# enumerate() returns a tuple with the index and the value from the iteratable at that index
for idx, n in enumerate(range(myStart, myEnd+1)):
    print(f'n[{idx}] = {n}')

print('\ncreate objects from another module and print them by leveraging their __str__ override')
from MyPoint import MyPoint
myFirstPoint = MyPoint(1, 2)
mySecondPoint = MyPoint(1, 2)
print(myFirstPoint)
print(mySecondPoint)

print('\ncompare objects by value and by reference')
print(f'myFirstPoint == mySecondPoint ? {myFirstPoint == mySecondPoint}')
print(f'myFirstPoint is mySecondPoint ? {myFirstPoint is mySecondPoint}')

print('\nmodify the class attribute, and show its effect on both objects')
MyPoint.rebase(1, 1)
print(myFirstPoint)
print(mySecondPoint)
