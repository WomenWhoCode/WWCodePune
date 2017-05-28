#a = [1, 2, 3]
# print(a)
# print(type(a))

#a = [1, 2.5, 'a', 2, 3, 4, 5, 6]
# print(a)

#print('0th element', a[0])
#print('last element', a[-1])

# difference between lists in python and C arrays
# list comprehension
# List methods:
#len, max, min, append, count(), extend, index, pop, pop(index), remove, reverse, sort, list 
# = operator does a sallow copy
#copy - deep copy for normal lists, shallow copy for a list of list

#Deepcopy import: from copy import deepcopy
 
# Time Complexity 

# in opertor
#print('Between first and last')
# for i in a:
#    pass
# print(i)

# not in operator
#b = 10
# if b not in a:
#    print('boom')
# else:
#    print('toom')

# is operator
# for i in a:
#    if b is i:  # python drawback oer C: duct typing
#        print('mil gaya')

#a == b implies hash(a) == hash(b)  (the reverse might not hold in the case of a hash collision).


# for loops over an array in C
# eg: element except first one
# in python
# print(a[1:])

# eg: element except last one
# print(a[0:-1])

# all elements
# print(a[:])

# Exercise-  eg: element except first and last

# Step operator
# print(a[::2])

# Exercise: Find the numbers at even places in list

# range function
#range(5)
#range(0,5)
#range(0,5,1)


#print(a + [7])

# Dictionary

#a = {'a': 1, 'b': 2}
#print('Dict', a)
# print(type(a))


#a = {1: 'a', 99: '10', '87': 'xyz'}
# print(a[1])
# print(a[99])
# print(a['87'])
# print(a[0])


# list of dictionaries
# dictionary of dictionaries
# JSON

# dict methods - clear, copy, len, fromkeys, get, items-> returns a list of tuples type dict_items, keys, values, update
# default copy is deep for normal dict, but shallow for nested ones

# From keys eg:
#a = {}
#a = a.fromkeys((1,2,3))
#a = a.fromkeys([1,2,3])
#a = a.fromkeys([1,2,3], 10)

# Tuples
# a = (1, 2, 3)
# a = 1, 2
# a = 1,
# print(a)
# print(a[0])
# mutability - the difference between tuple and lists

# tuple of tuples
# list of tuples
# dictionary of tuples

# Uses of tuple : faster than list, used in *args, return from built in fn
# methods - len, max, min, tuple

# Sets
a = {1, 2, 3, 4, 1, 2}
# print(a[0])
#a = {[1, 2, 3], 6, 7, 8}
#sets cant contain mutable objects, sets are mutable: 
#a.add(99)

#hash(a)

# methods - H.W.

# Hashing - time complexity involved in hash collisions, indexing, when its used in database

# class MutateHash(object):
#     def __init__(self, hash): # The object's hash will be hash
#         self.hash = hash
#     def __hash__(self):
#         return self.hash

# a = MutateHash(1)
# print('hash of a ',hash(a))

# b = {a:'10'}
# print('dict b 1', b[a])

# a.hash = 2
# hash(a)
# print('dict b 2', b[a])

# class Boom(object):
#     def __init__(self):
#         self.hashcounter = 0
#     def __hash__(self):
#         self.hashcounter += 1
#         return self.hashcounter

# a = Boom()
# s = {hash(a), hash(a), hash(a), hash(a), hash(a)}
# print('s', s)



# # Frozenset
# f = frozenset([1, 2])
# print('freeze', hash(f))

# a = {'k': f}
# print(a)

# a = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8]
# print(set(a))
# print(hash(a))

