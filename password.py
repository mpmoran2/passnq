import bcrypt

password = b"mypass" # we need this string in bytes so by adding b it is converted now to bytes
hashed = bcrypt.hashpw(password,bcrypt.gensalt()) # need to call on bcrypt and the hashpw method and to add salt, the .gensalt method
# print(hashed) # to make sure it hashed

# to allow for the password to be used while being hashed
entered_password = input('Please enter your password: ')
entered_password = bytes(entered_password, encoding='utf-8')

# use the checkpw method to see if both hashes match to validate user is correct
if bcrypt.checkpw(entered_password, hashed):
    print('Thank you, login successful. Sheepy granted access.')
else:
    print('We are sorry, access denied.')