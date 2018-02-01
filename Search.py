def getTokens(statament):
    return statament.split()

def findKeyword(token, listWords):
    return token in listWords

def getNameFileKW(zipName, lineNumber, keyWord):
    return zipName.split(".")[0] + "_line" + str(lineNumber) + "_" + keyWord + ".kwd"
