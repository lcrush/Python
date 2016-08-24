import hashlib
import uuid
#uuid is a randomizer for passwords and such

def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
#hashlib.sha256 is the amount of char that are going to be generated for the encoded password
#salt is the extra layer of encryption before the hash has been inputted into the encode

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

npass = input('What is it: ')
hashed_password = hash_password(npass)

print('Giberish you want to save: ' + hashed_password)

opass = input('Double check, re-enter: ')

if check_password(hashed_password, opass):
    print('Took long enough!')
    
else:
    print('Stooge try again!')
 
#Will run again if incorrect password is re-entered   
npass = input('What is it: ')
hashed_password = hash_password(npass)
    
print('Giberish you want to save: ' + hashed_password)
    
opass = input('Double check, re-enter: ')    

if check_password(hashed_password, opass):
    print('Took long enough!')
    
else:
    print('Stooge try again!')


