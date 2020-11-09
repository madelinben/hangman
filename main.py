def getFile():
    wordList = []
    with open("words.txt", "r") as file:
        for line in file:
            wordList.append(line.strip('\n'))

    print(wordList)


getFile()