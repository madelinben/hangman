import random


def getWord():
    wordList = []
    with open("words.txt", "r") as file:
        for line in file:
            wordList.append(line.strip('\n'))

    randomIndex = random.choice(wordList).upper()
    return randomIndex


def play():
    attemptCount = 6
    guessedCorrectly = False

    selectedWord = getWord()
    coveredWord = "_" * len(selectedWord)

    while not guessedCorrectly and attemptCount > 0:
        print(coveredWord)

        validateInput = True
        while validateInput:
            guess = input("Guess a character: ").upper()
            if len(guess) == 1 and guess.isalpha():
                for char in coveredWord:
                    if char == guess:
                        validateInput = False
                        print("Guess has already been attempted!")
            else:
                validateInput = False
                print("Provide a character value for a valid attempt!")

        validateAttempt = False
        for char in selectedWord:
            if char == guess:
                coveredWord += char
                validateAttempt = True
            elif char.isalpha():
                coveredWord += char
            else:
                coveredWord += "_"

        if validateAttempt:
            print("Correct Attempt! the character " + guess + " is located in the covered word.")
        else:
            print("Incorrect Attempt! the character " + guess + " is not located in the covered word.")

        if coveredWord == selectedWord:
            print("Congratulations! You've correctly guessed the covered word!")
            guessedCorrectly = True
            break

        attemptCount -= 1

    if not guessedCorrectly:
        print("Unlucky! You've run out of attempts and not guessed the covered word.\nThe word you were guessing was " + selectedWord)


play()
