# Reverse Cipheer
# https://www.nostarch.com/crackingcodes/(BSD Licensed)

def reverseCipher() -> str:
    translated: str = ''

    print('Enter message to be reversed:')
    myMessage: str = input() 

    i = len(myMessage) - 1
    while i >= 0:
        translated = translated + myMessage[i]
        i = i - 1

    return translated

if __name__ == '__main__':
    print(reverseCipher())