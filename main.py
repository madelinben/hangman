import random


def getWord():
    wordList = []
    with open("words.txt", "r") as file:
        for line in file:
            wordList.append(line.strip('\n'))

    randomIndex = random.choice(wordList).upper()
    return randomIndex


def play():
    attempts = 6
    finished = False

    selectedWord = getWord()
    guessWord = "_" * len(selectedWord)

    while not finished:
        finished = True


play()