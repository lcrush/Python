#Define the master list.Key
#What to do? Encode or Decode
#Endcode
#Decode
import string
import collections
#Definition Keys
plaintext = input('What do you want Secret Squirrel: ')

#alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = int(input('What is your shift: '))
cipher = ''

#Encryption/Decryption Code
def brutus(plaintext, key):
    #upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)    

    #upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    
    
for c in plaintext:
    if c in lower:
        cipher += lower[(lower(c) + key)%(len(lower))]
    

print('Morocco Mole hears: ' + cipher)