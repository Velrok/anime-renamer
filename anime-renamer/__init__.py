"""Anime Renamer

Anime renamer will try to find the anime name and episode number in the given
file. It will then rename / move the file. If you pass it a dest-folder
it will move the file to the given folder using the name schema:

<anime-name>_E<episode-number>.<extension>

Usage:
  anime-renamer <input-file> [dest-folder]


"""

from docopt import docopt


if __name__ == "__main__":
  args = docopt(__doc__)
  print args
  print "hello wordl"
