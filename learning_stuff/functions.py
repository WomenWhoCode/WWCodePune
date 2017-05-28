# def boom():
#     print('Hello')

# boom()


#a = 7
 
# def boom(a):
#     print('a',a)

# boom(a)
# a=10
# def boom(a=0):
#     print('a',a)

# boom(a)


# b = 10
# def boom(a,b):
#     print('a,b',a,b)

# boom(a,b)

# a=1
# b=100
# def boom(a,b):
#     print('a,b',a,b)
#b=9
# def boom(b=0):
    
    
#     print('b',b)
# boom()
# a=10
# c = 15
# b=5
# def boom(*args, **kwargs):
#     print('args', args[3])
#     print('kwargs', kwargs['first'])
    
# boom(1,2,3,4,5,first=10,second=20)
    
#a = range(10)
#for i in a:
#    print(i)

#boom()
# def boom(a,c,b=None):
#     print('a,b,c',a,b,c)


# def boom(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
#     print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)


# boom(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6)


def boom(*args):
    pass
   #print('args',args)
   #print('0th', args[0][0][1])
   #print('Answer this',args[-1]) [start:stop:step]
   #print('Answer this',args[:-9:2])
#boom([[1,2,3]],2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6)
#boom(range(30))  
#boom(*range(30))

# def boom(**kwargs):
#     print('kwargs', kwargs)
#     return 'boom called'

# #a = boom(b=1,c=2)

# print(boom(b=1,c=2)) 

# def boom(*args, **kwargs):
#     print('args, kwargs', args, kwargs)

# boom(10,20,b=1,c=2)



# Lambda functions
#def a(1):
#    return 1+1

#a = lambda x:x+1
#print(a(1))

#def a(x,y):
#    return x+y

#a = lambda x,y: x+y
#print(a(1,100))


# Uses of Lambda
# map, filter, lazy mood
#myth: considered as an optimized techinque
# show the bytecode of lambda and function

# map functions

def boom(a):
    return a+100


#map(function, iterative structure)

#a = map(boom, range(100)) # Guess how to resolve this error
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

# print(even([1,2,3,4,5,6,7,8,9]))


# partial solution
#print(map(lambda x:x if x%2==0 else None, [1,2,3,4,5,6,7,8,9]))


#print(filter(lambda x: x%2, [1,2,3,4,5,6,7,8,]))

# Using list comprehension
#print([x for x in [1,2,3,4,5,6,7,8,9] if x%2==0])


# Using (filter in map) using lambda
#Find the squares of the odd numbers in the list [1,2,3,4,5,6,7,8,9]
print(map(lambda x: x*x, filter(lambda x: x%2, [1,2,3,4,5,6,7,8,9])))




