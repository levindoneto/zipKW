
import zipfile
import os
import shutil

def extractZip(txt):
	sawyr74Zip = zipfile.ZipFile(txt)
	for data in sawyr74Zip.infolist():
		if data.filename.endswith('.txt'):
			sawyr74Zip.extract(data)
	sawyr74Zip.close()
