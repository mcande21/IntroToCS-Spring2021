# This program is going to load and crack a code
import string
import crypto

f = open('secret_message.txt', 'rb')
ciphertext = f.read().decode('ascii')
f.close()

for i in range(len(string.printable)):
    print(i, crypto.caesar_decrypt(ciphertext, i))

best_key = -1
best_total = -1
for i in range(len(string.printable)):
    # track the total words
    total = 0
    text = crypto.caesar_decrypt(ciphertext, i)
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
print("Final decryption:", best_key, crypto.caesar_decrypt(ciphertext, best_key))
