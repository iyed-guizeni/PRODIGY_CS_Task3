import string
import sys

password = input("enter your password")
#checking for uppercase
uppercase = any([1 if i in string.ascii_uppercase else 0 for i in password])

#checking for lowercase
lowercase = any([1 if i in string.ascii_lowercase else 0 for i in password])

#checking for digits
digit = any([1 if i in string.digits else 0 for i in password])

#checking for characters
characters = any([1 if i in string.punctuation else 0 for i in password])

#check if the password is in the TOP common password
with open("common.txt" , 'r') as f:
    common_password = f.read().splitlines()

if password in common_password:
    print(" The identified password is vulnerable to common attacks. It is strongly advised to promptly change it or enhance its security measures.")
    sys.exit()
score = 0
if len(password) >= 8:
    score+=1
if  uppercase == True :
    score+=1
if lowercase == True:
    score += 1
if digit == True:
    score += 1
if characters == True:
    score += 1
#assess password
if score <= 3 :
    print("password in weak ")
if score == 4 :
    print("password is good")
if score > 4:
    print("password is  strong ")







