"""
Caesar Cipher Brute Force Hacker

Attempts to crack Caesar cipher encrypted messages by trying all possible keys.
Based on code from https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""

from typing import List, Tuple
import argparse

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?.'

def decrypt_caesar_with_key(message: str, key: int, symbols: str) -> str:
    """
    Decrypt a Caesar cipher message using a specific key.
    
    Args:
        message: The encrypted message to decrypt.
        key: The shift value used for encryption (0 to len(symbols)-1).
        symbols: The character set used for encryption.
    
    Returns:
        The decrypted message string.
    """
    return ''.join([symbols[(symbols.find(symbol) - key) % len(symbols)] 
                if symbol in symbols else symbol 
                for symbol in message])

    # # It is important to set translated to the blank string so that the
    # # previous iteration's value for translated is cleared:
    # translated = []

    # # Loop through each symbol in the message:
    # for symbol in message:
    #     if symbol in symbols:
    #         symbol_index = symbols.find(symbol)
    #         translated_index: int = (symbol_index - key) % len(symbols)

    #         # Append the decrypted symbol:
    #         translated.append(symbols[translated_index])

    #     else:
    #         # Append the symbol without encrypting/decrypting:
    #         translated.append(symbol)
            
    # return ''.join(translated)


def hack_caesar_cipher(encrypted_message: str, symbols: str = SYMBOLS) -> List[Tuple[int, str]]:
    """
    Brute force decrypt a Caesar cipher by trying all possible keys.
    
    Args:
        encrypted_message: The encrypted message to crack.
        symbols: The character set to use (default: module-level SYMBOLS).
    
    Returns:
        A list of tuples containing (key, decrypted_message) for each possible key.
    """
    return [(key, decrypt_caesar_with_key(encrypted_message, key, symbols)) 
            for key in range(len(symbols))]

    # results = []
    
    # # Loop through every possible key.
    # for key in range(len(symbols)):

    #     # The rest of the program is almost the same as the Caesar cipher program:
    #     translated = decrypt_caesar_with_key(encrypted_message, key, symbols)
    #     results.append((key, translated))

    # return results

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Brute force decrypt a Caesar cipher by trying all possible keys.'
    )
    parser.add_argument(
        'message',
        nargs='?',  # Makes it optional
        default='guv5Jv5Jz!J5rp4r6Jzr55ntrM',  # Your test message as default
        help='The encrypted message to decrypt'
    )
    parser.add_argument(
        '-s', '--symbols',
        default=SYMBOLS,
        help='Custom symbol set to use (default: built-in set)'
    )
    return parser.parse_args()
    
if __name__ == "__main__":
    args: argparse.Namespace = parse_arguments()
    result: List[Tuple[int, str]] = hack_caesar_cipher(args.message, args.symbols)

    print(f"\nTrying all {len(SYMBOLS)} possible keys for: '{args.message}'\n")
    print("\n".join(f"Key {key}: {text}" for key, text in result))

"""
Optional Enhancements (if you want to take it further)
These are not necessary but could be interesting learning exercises:

Add a --key option to test a specific key instead of all 69
Add output filtering based on English word detection (using a dictionary)
Add a --verbose flag to show/hide the commented learning blocks
Export results to a file with --output filename.txt
Add unit tests in a separate file
"""