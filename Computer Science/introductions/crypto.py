# an exploraition of basic cryptography with some basic cyphers

import string
import random
import nltk
import util
import random
# tell nltk to download its words database
nltk.download("words")

# tell python to import the words database
from nltk.corpus import words

# extract a list of words from nltk
words = words.words()

def ceasar_encrypt(message, shift):
    """
    Enter a message using a caesar cypher
    :param message: clear (plain) text message
    :param shift: key for the cipher
    :return: ciphertext(encrypted message
    """
    ciphertext = ""
    # string.printable is a string constant of
    # every letter that python can print
    alphabet = string.printable
    for ch in message:
        # shift ch by the set amount
        # figure out where ch is in the alphabet
        chpos = alphabet.find(ch)
        # shift this position for our ciphertext
        # mod by length of alphabet so we stay within our string
        cipherpos = (chpos + shift) % len(alphabet)
        # append the character at cipherpos to our ciphertext
        ciphertext += alphabet[cipherpos]
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return ceasar_encrypt(ciphertext, -shift)

def substitution_encrypt(message, key):
    """
    Encrypt a message using a substituion cipher
    :param message: clear text
    :param key: scramble of the alphabet
    :return: cipher text (encrypted message)
    """
    alphabet = string.printable
    ciphertext = ""
    for ch in message:
        # replace the character with the character at the same position from our key
        # find the position of our character in our alphabet
        chpos = alphabet.find(ch)
        # append the character at the same position from the key
        ciphertext += key[chpos]
    return ciphertext

def substitution_decrypt(ciphertext, key):
    """
    Decrypt a message that was encrypted with a substitution cipher
    :param ciphertext: encrypted message
    :param key: scramble of alphabet
    :return: clear text message
    """
    alphabet = string.printable
    message = ""
    for ch in ciphertext:
        # decryption is the opposite of encryption
        chpos = key.find(ch)
        message += alphabet[chpos]
    return message

def otp_encrypt(message, key):
    """
    Encrypt message using one time pad
    :param message: clear text message
    :param key: random string the same length as message
    :return: ciphertext
    """
    alphabet = string.printable
    ciphertext = ""
    # loop over the indices rather than the character
    for i in range(len(message)):
        message_c = message[i]
        key_c = key[i]
        # get the positions from the alphabet
        message_pos = alphabet.find(message_c)
        key_pos = alphabet.find(key_c)
        # add together and mod by length
        cipher_pos = (message_pos + key_pos) % len(alphabet)
        # append the letter at this position to our ciphertext
        ciphertext += alphabet[cipher_pos]
    return ciphertext

def otp_decrypt(ciphertext, key):
    alphabet = string.printable
    message = ""
    for i in range(len(ciphertext)):
        cipher_c = ciphertext[i]
        key_c = key[i]

        cipher_pos = alphabet.find(cipher_c)
        key_pos = alphabet.find(key_c)

        message_pos = (cipher_pos - key_pos) % len(alphabet)

        message += alphabet[message_pos]
    return message


# MAIN PROGRAM
message = "yo! why yo butt so HARRY... Dawg"
key = random.randrange(len(string.printable))
encrypted_message = ceasar_encrypt(message, key)
decrypted_message = caesar_decrypt(encrypted_message, key)
print(encrypted_message)
print(decrypted_message)

# crack the key
for i in range(len(string.printable)):
    # try i as the shift
    print(i, caesar_decrypt(encrypted_message, i))
best_key = -1
best_total = -1
for i in range(len(string.printable)):
    # track the total words
    total = 0
    text = caesar_decrypt(encrypted_message, i)
    # split text into words
    sentence = text.split()
    for w in sentence:
        # checks if the word is english
        if w in words:
            total += 1

    # check to see if this is better than the best key
    if total > best_total:
        best_key = i
        best_total = total
        print("Best so far:", i, text)

# When the loop is done, best_key will contain the key that gave us most words
print("Final decryption:", best_key, caesar_decrypt(encrypted_message, best_key))

# substituion cipher
# key should be a scrambled version of the alphabet
substitution_key = util.scramble(string.printable)
sub_encrypted = substitution_encrypt(message, substitution_key)
print("Encrypted with substitution cipher:", sub_encrypted)
sub_decrypted = substitution_decrypt(sub_encrypted, substitution_key)
print("We decrypted:", sub_decrypted)

# one time pad --- an unbreakable cipher
# building up a key
otp_key = ""
for i in range(len(message)):
    # MAJOR SECURITY FLAW
    # random module is not actually random its pseudorandom numbers
    # need: actual randomness to make this unbreakable
    # "cryptographically secure" random numbers
    # python provides the 'secrets' module for more secure random numbers
    otp_key += string.printable[random.randrange(len(string.printable))]

print("Out otp key:", otp_key)
otp_encrypted_message = otp_encrypt(message, otp_key)
print("Encrypted with otp key:", otp_encrypted_message)

# write our incrypted message to a file
f = open("encrypted_message.txt", "w")
f.write(otp_encrypted_message)
f.close()