# Reverse Cipher
# https://www.nostarch.com/crackingcodes/(BSD Licensed)

message = input("Enter message: ")
translated: str = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    print("i is", i, ", message[i] is", message[i], ", translated is", translated)
    i = i - 1

print(translated)

