from os import listdir, stat
from os.path import join, isdir, basename
from glob import glob

def listFiles(path, pattern = '*'):
	files = []
	for f in glob(join(path, pattern)):
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