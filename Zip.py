
import zipfile
import os
import shutil

def extractZip(txt):
	sawyr74Zip = zipfile.ZipFile(txt)
	for data in sawyr74Zip.infolist():
		if data.filename.endswith('.txt'):
			sawyr74Zip.extract(data)
	sawyr74Zip.close()

def compressFolder(rootZip):
	zipFile = zipfile.ZipFile(rootZip.split(".")[0] + ".zip", "w")
	for dirname, subdirs, files in os.walk(rootZip.split(".")[0] + "-data"):
	    zipFile.write(dirname)
	    for filename in files:
	        zipFile.write(os.path.join(dirname, filename))
	zipFile.close()
