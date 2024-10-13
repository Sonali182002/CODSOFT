import string
import random
# this program creates a random password
print("**********Paasword Generator**************")
#this "choice" method form random library  will generate rate the randome lower and upper case letters 
letter=random.choice(string.ascii_letters)
print(letter)
print("which types of password you want to generate")
print("1.only Uppercase          2.Only lowercase")
print("3.Only Number             4.Mixture of all including special symbol")
UserChoice=input("Enter the your Choice 1/2/3/4: ")
length=int(input(("enter the desired length of password you want to generate: ")))
# we have taken a password as a String to store the generated password in it.
password=""
if(UserChoice=='1'):
    password=''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    # this for loop with the join method is used to generate only the user's desired lengthof password
    # join is string method in python which put or we can say join the characters together in a single string.
    # '' (no space) used with the join is "separator_string" which is placed between the each element that join method is putting in a string.
elif(UserChoice=='2'):
    password=''.join(random.choice(string.ascii_lowercase) for _ in range(length))
elif(UserChoice=='3'):
    password=''.join(random.choice('0123456789') for _ in range(length))
elif(UserChoice=='4'):
    password=''.join(random.choice(string.ascii_letters)+random.choice(string.punctuation) for _ in range(length))
else:
    print("Invalid Choice")    

print("generated password: ", password)    





