# This is a password generator whic would generate new passwords.
# Based on RANDOM fuction.
import string
# Imports a string for the program.
import random
# Imports the random function.
characters = string.ascii_letters + string.punctuation  + string.digits
# Adds random string Letters, Punctuations, and Digits.
password = ""
# Used to concatinate password as a string 

password_length = random.randint(8, 16)
# Sets the length of the password in between 8 to 16 digits
for x in range(password_length):
    char = random.choice(characters)
    password = password + char
# Random Function used
print (password)
# Prints the randomly generated password
print("is you new generated password")
# prints the above given string after printing the password
quit ()
# Ends the program




