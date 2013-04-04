import stat as stat2
from os import listdir, stat
from os.path import join, isfile, basename
from fnmatch import fnmatch

def listFiles(path, pattern = '*'):
  ''' recursivly search for all files matching the given pattern
      and returns all files beginning with the given path '''
  files = []
  for f in listdir(path):
    fpath = join(path, f)
    if isfile(fpath):
      if fnmatch(f, pattern):
        stats = stat(fpath)
        if stat2.S_ISREG(stats.st_mode):
          files.append({'filename': basename(fpath)
            , 'path': fpath
            , 'filesize': stats.st_size
            })
    else:
        files.extend(listFiles(fpath, pattern))
  return files