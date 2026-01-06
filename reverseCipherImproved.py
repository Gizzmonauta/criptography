# Reverse Cipher
# https://www.nostarch.com/crackingcodes/(BSD Licensed)

def reverse_cipher(message: str) -> str:
    """Reverse the order of characters in a message.
    
    Args:
        message: The string to reverse
        
    Returns:
        The reversed string
    """

    # Option 1: Pythonic slicing (fastest)
    return message[::-1]
    
    # Option 2: If you want to keep it educational with a loop,
    # use a list to build the result:
    # result = []
    # for i in range(len(message) - 1, -1, -1):
    #     result.append(message[i])
    # return ''.join(result)

def main():
    print("Enter a message to reverse: ", end="")
    message = input()
    print(reverse_cipher(message))

if __name__ == '__main__':
    main()