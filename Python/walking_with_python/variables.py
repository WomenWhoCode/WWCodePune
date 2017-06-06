a = 10

print("value of a", a)
print("type of a", type(a))

b = a
print("value of b", a)

from sys import getrefcount as grc

print(grc(a))
del a
print(grc(b))


# python 2
print(type(2**1000))

# python 3
print(type(2**1000))

# duct typing
a = "Women who code"

print(id(a))

a = a + "and learn"

print(id(a))


name = input("Give me your name: ")
print("Your name is " + name)
print("Your name is ", name)

print(name * 10)


"""
Exercises:
   a). Add 2 variables and print the result
   b). Print the result without using any variable
   c). Find the square root of any given number via input()
   d). Add 2 strings
   e). print a string 100 times
#  f). String slicing ( Will do its practice in
# lists datatype section)
"""
