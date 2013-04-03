from os import listdir
from os.path import join, isdir
from glob import glob

def listFilesPattern(path, pattern):
	files = []
	for f in glob(join(path, pattern)):
		files.append(join(path, f))
	for d in listdir(path):
		fpath = join(path, d)
		if isdir(fpath):
			files.extend(listFilesPattern(fpath, pattern))
	return files

def listFiles(path):
    files = []
    for f in listdir(path):
       	fpath = join(path, f)
       	if not isdir(fpath):
           	files.append(fpath)sd
       	else:
           	files.extend(listFiles(fpath))
    return files            