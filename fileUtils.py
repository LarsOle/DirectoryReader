from os import listdir, stat
from os.path import join, isdir, basename
from glob import glob

#function to scan the directories for all files in the folder and in the subfolder
def listFiles(path, pattern = ''):
	files = []
	for f in glob(join(path, pattern)):
		if isdir(f):
			break
		fpath = join(path, f)
		stats = stat(fpath)
		files.append({'filename': basename(fpath)
			, 'path': fpath
			, 'filesize': stats.st_size
			})
	for d in listdir(path):
		fpath = join(path, d)
		if isdir(fpath):
			files.extend(listFiles(fpath, pattern))
	return files
