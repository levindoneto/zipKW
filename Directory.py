import os
import ManagementFile

def getRootDirName(zipFile):
    return zipFile.split(".")[0] + "-data"

def walk(rootZip, rootDir, keywords):
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.endswith(".txt"):
                ManagementFile.manager(rootZip, os.path.join(root, file), keywords)

def getDirFiles(filePath):
    listPath = filePath.split("\\")
    path = ""
    for i in range(len(listPath) - 1):
        path += listPath[i] + "/"
    return path
