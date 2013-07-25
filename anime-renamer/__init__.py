"""Anime Renamer

Anime renamer will try to find the anime name and episode number in the given
file. It will then rename / move the file. If you pass it a dest-folder
it will move the file to the given folder using the name schema:

<anime-name>_E<episode-number>.<extension>

Usage:
  anime-renamer <input_file> [<dest_folder>]


"""

from docopt import docopt
import os.path

class RuntimeError(Exception):
  pass


def rename(filename, dest_folder):
  if not os.path.exists(filename):
    raise RuntimeError("file {} does not exist".format(filename))
  if dest_folder and (not os.path.exists(dest_folder)):
    raise RuntimeError("destination folder {} does not exist".format(dest_folder))


if __name__ == "__main__":
  args = docopt(__doc__)
  try:
    rename(args['<input_file>'], args['<dest_folder>'])
  except RuntimeError as e:
    print "RuntimeError:", e
