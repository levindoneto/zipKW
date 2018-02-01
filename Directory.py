import os
import ManagementFile

def getRootDirName(zipFile):
    return zipFile.split(".")[0] + "-data"
