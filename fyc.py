MAX_KEY_SIZE = 26


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
        print('How many nutz you got stashed (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

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