from os import listdir, stat
from os.path import join, isfile, basename
from stat import S_ISREG

enToIntern = {'Filename': 'filename'
            ,'Filesize': 'filesize'
            ,'Path': 'path'
            }

def listFiles(path):
  files = []
  for f in listdir(path):
    fpath = join(path, f)
    if isfile(fpath):
      stats = stat(fpath)
      if S_ISREG(stats.st_mode):
        files.append({'filename': basename(fpath)
          , 'path': fpath
          , 'filesize': stats.st_size
          })
    else:
        files.extend(listFiles(fpath))
  return files