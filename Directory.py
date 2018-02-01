import os
import ManagementFile

def getRootDirName(zipFile):
    return zipFile.split(".")[0] + "-data"

def walk(rootZip, rootDir, keywords):
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.endswith(".txt"):
                ManagementFile.manager(rootZip, os.path.join(root, file), keywords)
