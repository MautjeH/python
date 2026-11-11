import string
import random as r
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '[', ']', '{', '}', '/', '`', '-', '_', '=', '+', '<', '>', '~', '|', '?', '\'', '\"', '\\']
print(len(alphabet))



def encrypt(message, key):
    for i in range(len(message)):
        if i == 0:
            message[i] = alphabet[(alphabet.index(key[i%len(key)]) + alphabet.index(message[i])) % (len(alphabet))]
        else:
            x = alphabet.index(message[i-1])
            message[i] = alphabet[(alphabet.index(key[i%len(key)]) + alphabet.index(message[i]) + x) % (len(alphabet))]
    return "".join(message)
def decrypt(message, key):
    y = message.copy()
    for i in range(len(message)):
        if i == 0:
            message[i] = alphabet[((alphabet.index(message[i]) - alphabet.index(key[i%len(key)])) % len(alphabet))]
        else:
            x = alphabet.index(y[i-1])
            message[i] = alphabet[((alphabet.index(message[i]) - alphabet.index(key[i%len(key)]) - x) % (len(alphabet)))]
    return "".join(message)



def cipher(message, key):
    for i in range(len(message)):
        message[i] = alphabet[(alphabet.index(message[i]) + alphabet.index(key[i%len(key)])) % 26]
    return "".join(message)

def decrypt_cipher(message, key):
    for i in range(len(message)):
        message[i] = alphabet[(alphabet.index(message[i]) - alphabet.index(key[i%len(key)])) % 26]
    return "".join(message)




def worse_encrypt(message, key):
    for i in range(len(message)):
        if i == 0:
            message[i] = alphabet[(key + alphabet.index(message[i])) % (len(alphabet))]
        else:
            x = alphabet.index(message[i-1])
            message[i] = alphabet[(key + alphabet.index(message[i]) + x) % (len(alphabet))]
    return "".join(message)
def worse_decrypt(message, key):
    y = message.copy()
    for i in range(len(message)):
        if i == 0:
            message[i] = alphabet[((alphabet.index(message[i]) - key) % len(alphabet))]
        else:
            x = alphabet.index(y[i-1])
            message[i] = alphabet[((alphabet.index(message[i]) - key - x) % (len(alphabet)))]
    return "".join(message)


#encryptdecrypt = input("Do you want to encrypt or decrypt? ")
#method = input("wich way of encryption do you want to use? ")
message = list(input("Please input your message here: "))
#if encryptdycrypt == "encrypt" and method == "encrypt" or encryptdecrypt == "encrypt" and method == "cipher":
#   keykind = input("Do you want to use a random generated or custom key? ")
#   if keylength == "random generated":
#       key = []
#       keylength = input("What length key relative to the message (in percentage) do you want?")
#       for j in range(len(message) * (keylength / 100)):
#           key.append(alphabet[r.randint(0, len(alphabet) - 1)])
#       key = "".join(key)
#       print(f"your key is: {key}")
#   else:
#       key = input("input your key: ")


#elif encryptdycrypt == "decrypt":
#   if method == worse_decrypt:
#       key = input("input your key: ")
#       while not key.isnumeric():
#           key = input("invalid key: ")
#       key = int(key)
#   else:
#       key = input("input your key: ")



key = []
for j in range(len(message)):
    key.append(alphabet[r.randint(0, len(alphabet) - 1)])
key = "".join(key)
print(f"your key is: {key}")
#key = input("input your key: ")




print(encrypt(message, key))
#print(cipher(message, key))

print(decrypt(message, key))

#print(decrypt_cipher(message, key))