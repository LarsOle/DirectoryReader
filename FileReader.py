from os import listdir
from os.path import join, isdir
from glob import glob

def listFiles(path, pattern = '*'):
	files = []
	for f in glob(join(path, pattern)):
		files.append(join(path, f))
	for d in listdir(path):
		fpath = join(path, d)
		if isdir(fpath):
			files.extend(listFiles(fpath, pattern))
	return files