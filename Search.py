def getTokens(statament):
    return statament.split()

def findKeyword(token, listWords):
    return token in listWords

def getNameFileKW(zipName, lineNumber, keyWord):
    return zipName.split(".")[0] + "_line" + str(lineNumber) + "_" + keyWord + ".kwd"

def createHighlightedStatement(listWords, foundKeyword):
    statament = ""
    for i in range(len(listWords)):
        singleWord = ""
        if (listWords[i] == foundKeyword):
            singleWord = "**" + foundKeyword + "**"
        else:
            singleWord = listWords[i]
        statament += singleWord + " "
    return statament
