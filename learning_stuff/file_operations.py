file_object = open('boom.txt', 'r')

for i in file_object:
   print(i)

# what if I read it again?
#for i in file_object:
#   print(i+'--------')

#file_object = open('boom.txt', 'r')

#for i in file_object:
#    print(i)

# what if I read it again?
#for i in file_object:
#    print(i+'--------')

#file_object.close()


#file_object = open('boom.txt', 'w') # deletes the read reference
#file_object.write('-------------')

#file_object = open('boom.txt', 'a') 
#file_object.write('+++++++++++++++++++++++++++++')

#for i in file_object:
#    print('0', i) # As no reference is there for file_object for readding

#file_object.close() # Not necessary but a good practice

import os
print(os.getcwd())

#open it via path location
file_object = open('/home/arjunsingh/practice/WWC/WWCodePune/learning_stuff/boom.txt')
print(file_object.read())
file_object.close()

#import os
#print(os.getcwd())

# open it via path location
#file_object = open('/home/arjunsingh/practice/WWC/WWCodePune/learning_stuff/boom.txt')
#print(file_object.read())
#file_object.close()

#with open('boom.txt', 'r') as file_object:
#    print(file_object.read())

"""
Exercises:
Try r,r+,w,w+,a modes with file handling
"""