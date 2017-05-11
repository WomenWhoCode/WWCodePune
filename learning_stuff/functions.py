def boom():
    print('Hello')

#boom()


# a = 7

# def boom(a):
#     print('a',a)

# #boom(a)

# def boom(a=0):
#     print('a',a)

# #boom()


# b = 10
# def boom(a,b):
#     print('a,b',a,b)

# boom(a,b)


# def boom(a,b=None):
#     print('a,b',a,b)

# boom(a)

# c = 15

# #def boom(a,b=None,c):
# #    print('a,b,c',a,b,c)

# def boom(a,c,b=None):
#     print('a,b,c',a,b,c)


# def boom(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
#     print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)


# boom(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6)


#def boom(*args):
#    print('args',args)
#    print('0th', args[0])
#    print('Answer this',args[-1])
#    print('Answer this',args[:-1])
#boom(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6)
#boom(range(30))
#boom(*range(30))

# def boom(**kwargs):
#     print('kwargs', kwargs)

# boom(b=1,c=2)

# def boom(*args, **kwargs):
#     print('args, kwargs', args, kwargs)

# boom(10,20,b=1,c=2)



# Lambda functions

#a = lambda x:x+1
#print(a(1))

#a = lambda x,y: x+y
#print(a(1,1))


# Uses of Lambda
# map, filter, lazy mood
#myth: considered as an optimized techinque
# show the bytecode of lambda and function

# map functions

#def boom(a):
#    return a+100

# map(function, iterative structure)

#a = map(boom, 1) # Guess how to resolve this error
#print('a',a)


# using map with lambda
#print(map(lambda x: x+100, [1,2]))

#print(map(lambda x: x+100 if x<10 else x+1000, [1,2, 11]))

#print(map(lambda x: x+100 if x<10, [1,2, 11])) # A lambda must always return a value


# Using map as an identity function
#print(map(None, [1,2,3]))


# Filters
# def even(x):
#     temp = []
#     for i in x:
#         if i%2==0:
#             temp.append(i)
#     return temp

#print(even([1,2,3,4,5,6,7,8,9]))


# partial solution
#print(map(lambda x:x if x%2==0 else None, [1,2,3,4,5,6,7,8,9]))


#print(filter(lambda x: x%2, [1,2,3,4,5,6,7,8,]))

# Using list comprehension
#print([x for x in [1,2,3,4,5,6,7,8,9] if x%2==0])


# Using (filter in map) using lambda
# Find the squares of the odd numbers in the list [1,2,3,4,5,6,7,8,9]
#print(map(lambda x: x*x, filter(lambda x: x%2, [1,2,3,4,5,6,7,8,9])))



