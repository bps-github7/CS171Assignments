##Ben Sehnert---bps53@drexel.edu---12455911
##CS172
##Professor D. Augenblick

##HW1 socialite user interface

#import statement
from Socialite import *

def socialite_creator():
    '''
prompts the user for input and plugs those values into the setter methods of the socialite class.
Takes no parameters. Returns socialite account info as a string
    '''
    #Boolean value set to True for loop variable
    loop = True;
    #uses above boolean to loop until that variable is set to true
    while loop:
        #user facing input prompt
        lastName = input('Enter the last name for Socialite:\n');
        #setter 
        s.setLastName(lastName);
        #breaks free from the loop
        loop = False;
    #First name
    loop = True;
    while loop:
        FirstName = input('Enter the first name for Socialite:\n');
        s.setFirstName(FirstName);
        loop = False;
    #picture
    loop = True;
    while loop:
        picture = input('Enter picture for Socialite:\n');
        s.setPicture(picture);
        loop = False;
    #website
    loop = True;
    while loop:
        website = input('Enter the Website URL for Socialite:\n');
        s.setWebsite(website);
        loop = False;
    #description
    loop = True;
    while loop:
        Description = input('Enter the description of the URL for Socialite:\n');
        s.setDescription(Description);
        loop = False;
    #UserID verification and settter method
    loop = True;
    while loop:
        userID = input('Enter the user ID for Socialite:\n');
        s.setUserID(userID);
        loop = False;
    #saves the object output into variable
    string = s.__str__();
    #returns the variable
    return string;

print("Welcome to the Socialite generator");#user interface begings.
loop = True;#sets boolean to True
while loop:#loops until user inputs the correct input type and ammount
    count = input("Enter the amount of socialite accounts you would like to create: \n")#input prompt
    try:
        count = int(count)#tests to see that user inputed correct type
    except ValueError: #exception block
        print("You must enter an integer(whole number)")
        continue
    if int(count) > 5: #Checks to see if user inputted a number less than five. We did this so that users cannot input infintesimal accounts
        print("For security purposes, only five accounts can be created at a time.\nPlease try again")
    else:
        print('We will now make',count,'socialite accounts'); #tells the user what will happen next
        loop = False #escapes loop now that input was succesully recieved

container = [] #list for storing results of account creation function
count = int(count) #type casts the amount inputted by the user so it can be used by for loop

for i in range(1,count+1): #loops over the amount of times the user wants to create an account
    s = Socialite() #initializes object of the class socialite
    one = socialite_creator() #stores results of socialite creator function in a variable
    container.append(one) #appends the variable to a list

print("{:=^100s}".format("Socialite Accounts:"))#header for print out section
for entries in container: #loops over the indexes of outer loop
    for i in entries: #loops over the indexes of inner loop-  __str__ returns a list with account info inside
        print(i)#outputs account info
