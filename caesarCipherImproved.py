# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip
from typing import List, Dict, Literal

# Define the symbols that can be encrypted/decrypted
SYMBOLS: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?.'
symbol_to_index: Dict[str, int] = {char: idx for idx, char in enumerate(SYMBOLS)}
index_to_symbol: Dict[int, str] = {idx: char for idx, char in enumerate(SYMBOLS)}

def caesar_cipher(message: str, key: int, mode: Literal['encrypt', 'decrypt']) -> str:

    # Store the encrypted/decrypted form of the message:
    translated: List[str] = []

    # Validate mode
    if mode not in ('encrypt', 'decrypt'):
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")

    for symbol in message:
        # Note: Only symbols in SYMBOL_SET can be encrypted/decrypted.
        if symbol in symbol_to_index:
            symbol_index: int = symbol_to_index[symbol]

            # Perform the encryption/decryption with automatic wrap-around
            if mode == 'encrypt':
                translated_index: int = (symbol_index + key) % len(SYMBOLS)
            elif mode == 'decrypt':
                translated_index: int = (symbol_index - key) % len(SYMBOLS)

            translated_symbol: str = index_to_symbol[translated_index]
            translated.append(translated_symbol)

        else:
            # Append the symbol without encrypting/decrypting:
            translated.append(symbol)

    return ''.join(translated)

def main() -> None:
    message: str = input("Enter the message you want to encrypt/decrypt: ")
    key: int = int(input("Enter the key (number): "))
    mode: str = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ")
    result: str = caesar_cipher(message, key, mode)
    print(result)
    pyperclip.copy(result)

if __name__ == "__main__":
    main()