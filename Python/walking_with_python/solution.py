# 1).
"""
a = 10
print(type(a))
a = '10'
print(type(a))
a = 10.0
print(type(a))
a = 10,
print(type(a))
a = [10]
print(type(a))
a = {10:10}
print(type(a))
a = {10}
print(type(a))

"""

# 2).
"""
a = 10
if(type(a)=='string'):
    print('I am a string')
elif(type(a)=='int'):
    print('I am an integer')
# Find out the reason of using an elif instead of else
"""

# 3).
"""
from sys import getrefcount as grc
a = 1
b = a
print('Ref count of a,b', grc(a),grc(b))
a = 2
print('Ref count of a,b', grc(a),grc(b))
"""

# 4).
"""
a = [9,8,7]
print('First element: ',a[0])
print('Last element: ',a[-1])

# What if the list is empty?
if len(a)>0:
    print('First element:{0}, Last element:{1}'.format(a[0], a[-1]))
print('List empty')
"""

# 5).
"""
a = [1,2,3,4]
b = [5,6,7,8]
print(a+b)
"""


# 6).
"""
a = [1,2,3,4,1,2,3,4]
a = set(a)
print('set',a)
print('Address of set', id(a))
"""

# 7). 
"""
a = [1,2,3,4,5,6,7,8,9]
#a.remove(9)
#a.remove(a[-1])
#a.remove(a[a.index(a[-1])])
#a.pop()
#del a[8]
#del a[-1]
#del a[a.index(a[-1])]
"""

# 8).
"""
a = [9,8,1,3,4,7,6,5,2]
a.sort()
print('Sorted list', a)
"""

# 9).
"""
a = [{1:1, 2:2}, {'1':1, 3:3, 4:4}, {1.1:10, 5:5, 6:6}]
print('list of dictionaries')
print('a[0][1]',a[0][1])
print("a[1]['1']",a[1]['1'])
# Find out the difference between '''  and "" and '' and the reason of using "" over '' in print()
"""

# 10).
"""
a = [(1,2,3), (4,5,6), (7,8,9)]
print('List of tuples', a)
for i in a:
    print(i)
[print(i) for i in a]
"""

# 11).
"""
a = [1,2,3,4]
for i in a:
    print(i*i)
[print(i*i) for i in a]
"""

#12).
"""
for i in a:
    if(i%2!=0):
        print(i)
[print(i*i) for i in a if i%2!=0]
"""

# 13).
"""
# variables are always deep copy
a = [1,2,3]
b = a
print('Before changing a,b', a,b)
b.append(4)
print('After changing b, value of a,b', a,b)

print('copy method does a deep copy for non nested lists and a shallow copy for the nested ones')
a = [1,2,3]
b = a.copy()
b.append(4)
print('After changing non nested b, value of a,b', a,b)
a = [1,2,3,[4,5,6]]
b = a.copy()
b[3][0] = 99
print('After changing nested b, value of a,b', a,b)

from copy import deepcopy
a = [1,2,3,[4,5,6]]
b = deepcopy(a)
b[3][0] = 99
print('After changing nested b in deep copy, value of a,b', a,b)

# Similarly for dictionary
"""

#14).
"""
a = [0,1,2,3,4,5,6,7,8,9,10]
for i in a[1:-1]:
    if(i%2==0):
        print(i)
[print(i) for i in a[1:-1] if i%2==0]
"""

#15).
"""
a = [1,2,15]
#i).
print(15 in a)

#ii).
if 15 in a:
    print(True)
"""

# 16).
"""
a = [1,10,20,2,3,50,40,10,9,60,70,90]

for i in a:
    if i>a[0] and i>a[1] and i>a[2]:
        print(i)
# Find out why we didnt use or operator

for i in a[3:]:
    if i>a[0] and i>a[1] and i>a[2]:
        print(i)

[print(i) for i in a[3:] if i>a[0] and i>a[1] and i>a[2]]

[print(i) for i in a[3:] if i>max(a[:3])]
"""

# 17).
"""
a = {1:1, 1:2}
print(a)
"""

#18).
"""
a = {1:1, 2:2, 3:3}
b = {}
for i in a:
    b[i] = a[i]
print(b)
"""

# 19).
"""
a = {}
for i in range(1,51):
    a[i]=100
print(a)

a = a.fromkeys(range(1,50), 100)
print(a)
"""

# 20).
"""
for i in range(1,51):
    a[i]=hash(i)
print(a)
"""

# 21).
"""
a = [1,2,3,3,4,5,6,6,6,6,7,8,0]
a = set(a)
print(a)
"""

# 22).
"""
a = [1,2,3,3,4,5,6,6,6,6,7,8,0]
a = set(a)
print(a[0])
print(hash(a))
"""

# 23).
"""
a = {1,2,3,4,4,5,5}
a.add(6)
a.pop()
print(a)
"""

# 24).
"""
a = frozenset([1,2,3])
print(hash(a))
a.add(4)
"""

# 25).
"""
a = [1,2,3,3,4,5,6,6,6,6,7,8,0]
a = tuple(a)
"""

#26).
"""
a = (1,2,3,3,4,5,6,6,6,6,7,8,0)
print(a[0])
print(hash(a))
print(hash(a[0]))
"""
