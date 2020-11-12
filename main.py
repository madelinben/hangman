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


play()
