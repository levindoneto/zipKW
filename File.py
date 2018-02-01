def readFile(fileInput):
    with open(fileInput) as f:
        listLines = f.readlines() # List of lines
        return listLines

def createFileKW (filename, highlightedStatament):
    fileKW = open(filename, "w+")
    fileKW.write(highlightedStatament)
    fileKW.close()
