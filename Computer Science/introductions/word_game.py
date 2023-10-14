# word game where the user has to guess a scrambled word

import util

#words = ["brownie", "biology", "craziness", "poopybutt"]
# read words from a file
words = []
f = open("words.txt")
for line in f:
    word = line.rstrip()
    # append this word to the list
    words.append(word)
# close the file
f.close()
for word in words:
    scramble = util.scramble(word)

    print("Guess the word from this scramble:", scramble)
    guess = input("Enter guess:")

    # check if the guess is correct
    if guess == word:
        print("No way you got it")
    else:
        for i in range(10000):
            print("No.")
        exit()

