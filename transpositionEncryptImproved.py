# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip
import argparse


def encrypt_message(key: int, message: str) -> str:
    """
    Encrypts a message using a transposition cipher.
    
    The cipher works by writing the message in rows of 'key' length,
    then reading columns vertically to create the ciphertext.

    Args:
        key: Number of columns to use in the transposition grid.
             Must be >= 1 and < len(message).
        message: The plaintext message to encrypt (non-empty).

    Returns:
        The encrypted ciphertext string.

    Raises:
        ValueError: If key < 1, message is empty, or key >= len(message).

    Time Complexity: O(n) where n = len(message)
    Space Complexity: O(n) for storing the result
    
    Example:
        >>> encrypt_message(3, "HELLO")
        'HLOEL'
        >>> encrypt_message(8, "Common sense is not so common.")
        'Cenoonommstmme oo snnio. s s c'
    """
    # Validate inputs
    if key < 1:
        raise ValueError("Key must be at least 1")
    if not message:
        raise ValueError("Message cannot be empty")
    if key >= len(message):
        raise ValueError(f"Key ({key}) must be less than message length ({len(message)})")

    # Build columns directly without initializing empty lists first
    cipher_text: list[list[str]] = [list(message[column::key]) for column in range(key)]

    # # Each string in cipher_text represents a column in the grid:
    # cipher_text: List[List[str]] = [[] for _ in range(key)]

    # # Loop through each column in cipher_text:
    # for column in range(key):
    #     cipher_text[column] = list(message[column::key])

        # # Keep looping until current_index goes past the message length:
        # while current_index < len(message):
        #     # Place the character at current_index in message at the end
        #     # of the current column in the cipher_text list:
        #     cipher_text[column].append(message[current_index])

        #     # Move current_index over:
        #     current_index += key

    # Convert the cipher_text list into a single string and return it:
    return ''.join(''.join(column) for column in cipher_text)

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Encrypt a message using a transposition cipher.'
    )
    parser.add_argument(
        'message',
        type=str,
        nargs='?',  # Makes it optional
        default='Common sense is not so common.',
        help='The message to encrypt (default: "Common sense is not so common.")'
    )
    parser.add_argument(
        'key',
        type=int,
        nargs='?',  # Makes it optional
        default=8,
        help='The number of columns to use in the transposition grid (default: 8)'
    )
    return parser.parse_args()

def main() -> None:
    """
    Main function that demonstrates transposition cipher encryption.

    Encrypts a sample message using a transposition cipher with a specified key,
    then displays and copies the result to the clipboard.

    The function:
    1. Defines a sample message and encryption key
    2. Encrypts the message using the encrypt_message function
    3. Prints the encrypted text with a pipe character (|) to show trailing spaces
    4. Copies the encrypted text to the system clipboard using pyperclip

    Example:
        Running this function will encrypt 'Common sense is not so common.'
        with key 8, print the result followed by '|', and copy it to clipboard.
    """
    args: argparse.Namespace = parse_arguments()

    try:
        cipher_text: str = encrypt_message(args.key, args.message)

        # Print the encrypted string in cipher_text to the screen, with
        # a | (pipe) after it in case there are spaces at
        # the end of the encrypted message:
        print(cipher_text + '|')

        # Copy the encrypted string in cipher_text to the clipboard.
        pyperclip.copy(cipher_text)

    except ValueError as ve:
        print(f"Error: {ve}")
        return

# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()