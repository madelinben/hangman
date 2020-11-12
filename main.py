import random


def getWord():
    wordList = []
    with open("words.txt", "r") as file:
        for line in file:
            if " " not in line:
                wordList.append(line.strip('\n'))

    randomIndex = random.choice(wordList).upper()
    return randomIndex


def play():
    attemptCount = 6
    guessedCorrectly = False

    selectedWord = getWord()

    coveredWord = "_" * len(selectedWord)
    previousGuesses = []

    while not guessedCorrectly and attemptCount > 0:
        print(coveredWord + "\n" + selectedWord)
        guess = input("Guess a character: ").upper()

        if len(guess)==1 and guess.isalpha():
            if guess in previousGuesses:
                print("Guess has already been attempted!")
            elif guess not in selectedWord:
                print("Incorrect Attempt! the character " + guess + " is not located in the covered word.")
                attemptCount -= 1
                previousGuesses.append(guess)
            else:
                print("Correct Attempt! the character " + guess + " is located in the covered word.")
                previousGuesses.append(guess)


play()
