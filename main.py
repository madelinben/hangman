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
    selectedWord = getWord()
    coveredWord = "_" * len(selectedWord)

    while not attempts > 0:

        validateAttempt = True
        while validateAttempt:
            guess = input("Guess a character: ").upper()
            if len(guess) == 1 and guess.isalpha():

                for char in coveredWord:
                    if char == guess:
                        validateAttempt = False
                        print("Guess has already been attempted!")
            else:
                validateAttempt = False
                print("Invalid attempt! Provide a character value for a valid attempt.")


play()
