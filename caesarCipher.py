# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = "This is my secret message."

# The encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts:
mode = 'encrypt'  # Set to 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in SYMBOLS can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform the encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle the wrap-around if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)