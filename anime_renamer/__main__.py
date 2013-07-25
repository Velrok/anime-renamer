"""Anime Renamer

Anime renamer will try to find the anime name and episode number in the given
file. It will then rename / move the file. If you pass it a dest-folder
it will move the file to the given folder using the name schema:

<anime-name>_E<episode-number>.<extension>

Usage:
  anime-renamer <input_file> [<dest_folder>]

"""
from docopt import docopt
from anime_renamer import rename

if __name__ == "__main__":
  args = docopt(__doc__)
  try:
    rename(args['<input_file>'],
           args['<dest_folder>'])
  except RuntimeError as e:
    print "RuntimeError:", e
