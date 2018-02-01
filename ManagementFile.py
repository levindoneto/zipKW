import File
import Search
import Directory

def manager(rootZip, filePath, keywords):
    lines = File.readFile(filePath)
    pathFile = Directory.getDirFiles(filePath)
    for i in range(len(lines)):
        tokens = Search.getTokens(lines[i])
        for j in range(len(keywords)):
            if (Search.findKeyword(keywords[j], tokens)): # A kw has been found
                filenameKW = Search.getNameFileKW(rootZip, i + 1, keywords[j])
                newStatement = Search.createHighlightedStatement(tokens, keywords[j])
                File.createFileKW (pathFile + "/" + filenameKW, newStatement)
