""""
 validate user input exercise
 1. Username is no more than 12 characters
 2. Username must not contain spaces
 3. Username must not contain digits
"""
username = input("Enter a username ")

if len(username) > 12:
    print("name must not contain more than 12 characters")
elif not username.find(" ") == -1:
    print("name must not contain any space in between")
elif not username.isalpha():
    print("name must not contain any digit")
else:
    print(f"Nice {username} your name has been inserted correctly")
