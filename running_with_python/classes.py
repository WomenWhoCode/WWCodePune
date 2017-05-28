class WomenWhoCodeMember(object):
    
    raise_seats = 1  # class variable
    #Encapsulation
    _private_variable = 2 # Nothing Private, just for developers to know that it is assumed to be private
    __super_private = 10 # Treated as the real private ones, as Python prepends the class name before that variable name, just in case you have 2 variables with same name
    #__init__() Double underscore methods(dunderscore) methods: Built in methods Reserved by python
    

    # def __init__(self, first, last, seats):
    #     self.first_name = first # instance methods
    #     self.last_name = last
    #     self.seats = seats
    #     self.email = first+'.'+last+'@g.com'


    def __init__(abc, first, last, seats):
        abc.first_name = first
        abc.last_name = last
        abc.seats = seats
        abc.email = first+'.'+last+'@g.com'

    
    def increaseSeats(self):
        self.seats = self.seats+self.raise_seats

        
    def fullName(self):
        return self.first_name+self.last_name

    @staticmethod
    def noArg_0():
        return 'Boom'

    
    @staticmethod
    def noArg_2(self): 
        return self.first_name

    @classmethod
    def set_number_of_seats_to_be_increased(cls, amount):
        cls.raise_seats = amount

    @classmethod
    def fromString(cls, member_str): 
        first, last, seats = member_str.split('-')
        return cls(first, last, seats) # alternative constructor
    
    
    @staticmethod
    def noArg_1(self):
        print('self', self)
        return 'Boom'

    
def noArg_1():
    print('Boom ----------------')
        
member_1 = WomenWhoCodeMember('AJ', 'Y', 1)
member_2 = WomenWhoCodeMember('AJ', 'Y', 2)



#print('class.__dict__', WomenWhoCodeMember.__dict__)

member_1.first_name= 'AJ'
member_1.last_name = 'Y'
member_1.email = 'aj.y@g.com'
member_1.seats = 1

#print('member_2', member_1.seats)
#print('Accessing class variable from instance',member_1.raise_seats)
#print('Accessing class variable from class',WomenWhoCodeMember.raise_seats)

#print('Instance __dict__',member_1.__dict__) # Class variable isnt in the instance object
#print('Class __dict__',WomenWhoCodeMember.__dict__)

#print('super private value', member_1._WomenWhoCodeMember__super_private)


#Changing the class variable's value
# WomenWhoCodeMember.raise_seats = 2
# print('Changing class variable value for Member 1 instance',member_1.raise_seats)
# print('Member 2 instance value is',member_2.raise_seats)
# print('Class Variable value', WomenWhoCodeMember.raise_seats)

# Suppose each member is bringing another person with him/her, therefore instead of changing each member's seats value, we change the whole class's variable 
#print('Changing the Class\'s Variable value')
#WomenWhoCodeMember.raise_seats = 2
#print('WomenWhoCodeMember 1 instance',member_1.raise_seats)
#print('WomenWhoCodeMember 2 instance',member_2.raise_seats)
#print('Class\'s Variable value', WomenWhoCodeMember.raise_seats)
# Even though member 1 was instantiated with raise_value of 1, it was changed as we changed the class variable of the whole class i.e. it inherits the class variable from the class


# Increasing seats via method using class variable
#print('Before increasing seats of instance 1', member_1.seats)
#member_1.increaseSeats()
#print('After increasing seats of instance 1', member_1.seats)



# Static Method

#print(member_1.email)


#member_1.fullName()
#print(member_1.fullName)
#print(WomenWhoCodeMember.fullName(member_1))
#print(WomenWhoCodeMember.fullName())

#print(member_1.fullName(member_1))

#print(member_1.noArg_0())
#print(WomenWhoCodeMember.noArg_0())
#print(WomenWhoCodeMember.noArg_1(member_1)) # There is  a difference between a static method and a global function


#print(member_1.noArg_1('a')) # Here 'a' is passed as self as something needs to be passed as I have mentioned that noArg_1 needs 1 argument and noArg_1 is also a static method


# accessing the instance values in a static method
#print('------------',member_1.noArg_2(member_1))





#classmethod/Alternative constructor


#print('Before changing raise amount:')
#print('Class variable',WomenWhoCodeMember.raise_seats)
#print('member_1 instance', member_1.raise_seats)
#print('member_2 instance', member_2.raise_seats)

# print('After calling class method and changing the raise amount')
# WomenWhoCodeMember.set_number_of_seats_to_be_increased(5)
# WomenWhoCodeMember.raise_seats = 5
# member_1.set_number_of_seats_to_be_increased(5) # Not preferred
# print('Class variable',WomenWhoCodeMember.raise_seats)
# print('member_1 instance', member_1.raise_seats)
# print('member_2 instance', member_2.raise_seats)


# Use of classmethod as an alternative constructor
#member_str_1 = "Arjunsingh-Yadav-1"
#member_str_2 = "Janki-Chhatbar-2"
#member_str_3 = "Sonal-Bobde-3"

#first, last, seats = member_str_1.split('-')
#new_member_1 = WomenWhoCodeMember(first, last, seats)
#print('New Member 1', new_member_1.email)


#new_member_2 = WomenWhoCodeMember.fromString(member_str_2) 
#print('New Member 2 using fromString', new_member_2.email)



# class MutateHash(object):
#     def __init__(self, hash):
#         self.hash = hash
#     def __hash__(self):
#         return self.hash

# a = MutateHash(2)
# print('Hash of object',hash(a) )

# b = {a:'10'}
# print('dict b 1', b[a])


# a.hash=1  #hash of object a is not changed, hence no difference in locating that object
# hash(a)
# print('dict b 2', b[a])


#a.hash=4  # Changing hash of a
#hash(a)
#print('dict b 3', b[a])

#Therefore mutability is tha main problem of hashing, as the new hash has to be adjusted in the existing hash table changing other elements position too thereby taking more time.
#Hence mutable data types are avoided in dictionary keys


# class Boom(object):
#     def __init__(self):
#         self.hashcounter = 0
#     def __hash__(self):
#         self.hashcounter += 1
#         return self.hashcounter

# a = Boom()
# s = {hash(a), hash(a), hash(a), hash(a), hash(a)}
# print('s', s)



