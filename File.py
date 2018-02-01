def readFile(fileInput):
    with open(fileInput) as f:
        listLines = f.readlines() # List of lines
        return listLines
