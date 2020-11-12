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

    coveredWord = ["_"] * len(selectedWord)
    previousGuesses = []

    while not guessedCorrectly and attemptCount > 0:
        print("Attempts Left: " + str(attemptCount) + "\nCovered Word: " + "".join(coveredWord) + "\t" + selectedWord)
        guess = input("Guess a character: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in previousGuesses:
                print("Guess has already been attempted!")
            elif guess not in selectedWord:
                print("Incorrect Attempt! the character " + guess + " is not located in the covered word.")
                attemptCount -= 1
                previousGuesses.append(guess)
            else:
                print("Correct Attempt! the character " + guess + " is located in the covered word.")
                previousGuesses.append(guess)

                for i in range(len(selectedWord)):
                    if selectedWord[i] == guess:
                        coveredWord[i] = guess

                if "_" not in coveredWord:
                    guessedCorrectly = True

    if guessedCorrectly:
        print("Congratulations! You've correctly guessed the covered word " + selectedWord + "!")
    else:
        print(
            "Unlucky! You've run out of attempts and not guessed the covered word.\nThe word you were guessing was " + selectedWord + "!")

    valid = False
    while not valid:
        userInput = input("Play again [y/n]").lower()
        if userInput == "y":
            valid = True
            play()
        elif userInput == "n":
            valid = True
            quit()
        else:
            print("Error! Value must be either y/n")


play()
