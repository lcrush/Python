MAX_KEY_SIZE = 26
#even = key[::2]
#index.odd = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
#index.even = (0, 2, 4, 6, 8, 10 , 12, 14, 16, 18, 20)



def getMode():#Function of encoding or decoding.
    while True:
        print('The F do you want?')
        mode = input().lower()
        if mode in 'buying b selling s'.split():
            return mode
        else:
            print('Enter either "buying" or "b" or "selling" or "s".')

def getMessage():#Inputs what you want encoded or decoded.
    print('Spit it out:')
    return input()

def getKey():
    key = 0
    while True:
        print('How many nutz you got stashed in the left (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        #for the odd index positions

#abcdefghijklmnopqurstuvwxyz

        print('How many nutz you got stashed in the right (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        #for the even index positions

def getTranslatedMessage(mode, message, key):#Gets it to keep upper and lower case letters.
    if mode[0] == 's':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                
            translated += chr(num)
        else:
            translated += symbol
    return translated

#How to differentiate the even and odd indexes to be asked for different key numbers 

mode = getMode()
message = getMessage()
key = getKey()

print('Deez nutz:')
print(getTranslatedMessage(mode, message, key))