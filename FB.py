import string
import collections

def brutus(plaintext, key):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)    

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

plaintext = str(input('What do you want Secret Squirrel: '))
key = int(input('What is your shift: '))
cipher = ''

#def brutus(plaintext, key):
 #   upper = collections.deque(string.ascii_uppercase)
  #  lower = collections.deque(string.ascii_lowercase)    

   # upper = ''.join(list(upper))
    #lower = ''.join(list(lower))

for c in str(plaintext):
    if c in upper:
        upper += upper[(upper(c) + key)%(len(upper))]
    elif c in lower:
        lower += lower[(lower(c) + key)%(len(lower))]
    

#return plaintext.translate(string.maketrans(stringascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

print('Morocco Mole hears: ' + cipher)