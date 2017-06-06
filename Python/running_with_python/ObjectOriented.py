from classes import WomenWhoCodeMember

class Developer(WomenWhoCodeMember, object):
    raise_amount = 20

    def __init__(self, *args, **kwargs):
    #def __init__(self, first, last, seats, prog_language):
        if 'members' in kwargs: # members causes problems in this init when creating Developer instance, but its needed in DevManager class while doing multiple Inheritance hence removing it from being passed to parent WomenWhoCodeMember when creating an instance of Developer and keeping it when creating an instance of DevManager
            #super().__init__(kwargs['first'], kwargs['last'], kwargs['seats'], kwargs['members'])
            super(Developer, self).__init__(kwargs['first'], kwargs['last'], kwargs['seats'], kwargs['members'])
        else:
            #super().__init__(kwargs['first'], kwargs['last'], kwargs['seats'])
            #super(Developer, self).__init__(kwargs['first'], kwargs['last'], kwargs['seats'])
            WomenWhoCodeMember.__init__(self, kwargs['first'], kwargs['last'], kwargs['seats'])
        # Instead of using If else, we can use default None to members
        
        #super(Developer, self).__init__(first, last, seats) # super(className, instance) in python 2.7 changed to no arguments in python 3 and passing object as an argument to class, useful in multiple inheritance
        # WomenWhoCodeMember.__init__(first, last, seats)

        self.prog_language = kwargs['prog_language']

class Manager(WomenWhoCodeMember, object):

    # def __init__(self, first, last, seats, members=None):
    #     super().__init__(first, last, seats)
    #     if members==None:
    #         self.members = []
    #     else:
    #         self.members = members

    def __init__(self, first, last, seats, members, **kwargs): # prefer using *args, **kwargs
        super().__init__(first, last, seats)
        self.members = members
    

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def print_members(self):
        if self.members:
            for member in self.members:
                print(member.fullName())
        else:
            print('No Member')

dev_1 = Developer(first='AJ', last='Yadav', seats=1, prog_language='Python')
dev_2 = Developer(first='Arjunsingh', last='Yadav', seats=2, prog_language='Java')

# print('Developer 1 seats',dev_1.seats)
# dev_1.increaseSeats()
# print('After increasing number of seats')
# print('Debeloper 1 seats',dev_1.seats)
# print('Developer 1 email',dev_1.email)
# print('Developer 1 Programming Language',dev_1.prog_language)


# mgr_1 = Manager('Sonal', 'Bobde', 50, [dev_1])
# mgr_2 = Manager('Janki', 'Chhatbar', 50, [dev_2])
# dummy_mgr = Manager('Vegeta', 'San', 0)


# print('Manager 1',mgr_1.email)
# print('Manager 1 Members: ')
# mgr_1.print_members()
# print('Manager 2',mgr_2.email)
# print('Manager 2 members')
# mgr_2.print_members()
# print('Dummy Manager', dummy_mgr.email)
# print('Dummy Manager members')
# dummy_mgr.print_members()



# mgr_1.add_member(dev_2)
# print('After Adding developer 2 in mgr 1')
# print('Manager 1 Members: ')
# mgr_1.print_members()
# print('After Deleting developer 1 in mgr 1')
# mgr_1.remove_member(dev_1)
# print('Manager 1 Members: ')
# mgr_1.print_members()



# MultiLevel Inheritance
# class DevManager(Developer, object): 

#     def __init__(self, first, last, seats, prog_language, hobbies):
#         super().__init__(first, last, seats, prog_language)
#         #super(DevManager, self).__init__(first, last, seats, prog_language)
#         self.hobbies = hobbies
        
# devMgr = DevManager('Goku', 'San', 10, 'KaMeHaMeHa', 'playing')

#print('Dev Manager', devMgr)
#print('dev mgr help', help(devMgr))
#print('Dev Manager Hobbies',devMgr.hobbies)
#print('Dev Manager Full Name: ', devMgr.fullName()) # Accessing method in parent's parent class i.w. WomenWhoCodeMember class



# Multiple Inheritance
class DevManager(Developer, Manager, object): # Creates a diamond problem, see its method resolution order; Actually it should be DevManager->Developer->WomenWhoCodeMember->Manager-WomenWhoCodeMember according to classic style classes in python <2.3, but from python >= 2.3 its flow is changed in C3 linerization to DM->Developer->Manager->WWCM
    
    #def __init__(self, first, last, seats, prog_language, members, hobbies):
    def __init__(self, *args, **kwargs):
        print('Inside DevMgr', args, kwargs)
        if kwargs:
            self.hobbies = kwargs.pop('hobbies') # Creates problem when classmethod calls classmethod, as we are passing just a string in that case
        # Either use Class 
        Developer.__init__(self, *args, **kwargs)
        Manager.__init__(self, **kwargs)

        # Or use Super, but for too complex inheritance use Class instead of super, as it involves the overhead of MRO and an issue of the arguments passed
        #super().__init__(*args, **kwargs)

        
    @classmethod
    def devMgrFromString(cls, *args, **kwargs):
        return cls(args, first=kwargs['first'], last=kwargs['last'], prog_language=kwargs['prog_language'], members=kwargs['members'], hobbies=kwargs['hobbies'], seats=kwargs['seats'])


    @classmethod
    def classMethodCallingClassMethod(cls, member_string):
        #return super(DevManager, cls).fromString(member_string) # Creates errors due to the arguments, so prefer using Class
        return WomenWhoCodeMember.fromString(member_string)

    
        
# devMgr = DevManager(first='Goku', last='San', seats=10, prog_language='KaMeHaMeHa', members=[dev_1, dev_2], hobbies='Watching DragonBall Anime')
# print('DevManager Name', devMgr.first_name)
# print('DevManager last Name', devMgr.last_name)
# print('DevManager Email', devMgr.email)
# print('DevManager Fullname', devMgr.fullName())


#print('Calling DevManager Classmethod')
#devmgrobj2 = DevManager.devMgrFromString(first='Richard', last='San', seats=10, prog_language='Python3.6', members=[dev_1, dev_2], hobbies='Watching Silicon Valley')

#calling WWCP classmethod-fromString from Devmgr classmethod- classMethodCallingClassMethod
member_str_1 = "Arjunsingh-Yadav-1"
WWCMObject = DevManager.classMethodCallingClassMethod(member_str_1)
print('WWCM email',WWCMObject.email)

