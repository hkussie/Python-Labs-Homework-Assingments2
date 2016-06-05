#this program asks a user if they would like a new password to be created
#if the user answers yes, a password will be created

import random

values = 'a1bcde348%#!04kjyt$*pvmq962tipjnc'
password = random.sample(values,10)

n = input("Would you like a newpassword: ")
if n == 'yes' or 'Yes':
    print("You're new password is: ", password)
else:
    print("A new password wasn't generated")


