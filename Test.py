import string
import collections

def brutus(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    
    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)
    
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    
    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

for i in range(len(string.ascii_uppercase)):
    print i, '|', brutus(our_string, i)