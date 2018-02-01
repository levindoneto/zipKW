import File
import Search
import Zip
import Directory

def manager(rootZip, keywords):
    Zip.extractZip(rootZip)
    rootDir = Directory.getRootDirName(rootZip)
    Directory.walk(rootZip, rootDir, keywords)
