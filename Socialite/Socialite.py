#Programmer: Ben Sehnert
#Program: Socialite class
#software purpose: Mock social media site
#Date: 7/30/2020

"""
Module level docstring: after a short requirements list is drafted,
we will need to re think the attributes and add helper methods.

For now, this class contains the bare minumum data for creating a profile
further iterations will need hashed, configurable password attribute and a mutable datatype
attribute that tracks profile info, followers/followees, groups and events.
"""

class Socialite(object):
    """
Class level docstring: class for tracking account holder info
for a small, mockup social media site.
    """
    version = 2.1

    #for now, password cannot be set via constructor
    def __init__(self, first, last, uID):   
        self.first_name = first
        self.last_name = last
        self.user_id = uID
        self._password = '*******'

    @property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, s):
        print("password cannot be edited")
        return 1

    def __str__(self):
        return "name: {} {}\nUserID: {}\npassword: {}"\
        .format(self.first_name, self.last_name, self.user_id, self._password)


def main():
    '''Simple unit test for Socialite methods'''
    test = Socialite('Ben', 'Sehnert', 12345)
    print(test.__str__())
    print("\nDisplaying current userID (get method testing):")
    print(test.user_id)
    print("\nGenerating new userID (set method testing):")
    test.user_id = 98765
    print(test.__str__())
    # Not working as expected. 
    # test.password = 'bilbo baggins'

#Intiailize testing..
if __name__ == "__main__":
    main()
