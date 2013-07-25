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
import re

class RuntimeError(Exception):
  pass


def extract_first(regex, string):
  pattern = re.compile(regex)
  match = pattern.search(string)
  if match:
    return match.groups()[0]
  else:
    return None

def filter_out(string, * matchers):
  result = string
  print string
  for matcher in matchers:
    print "applying ", matcher
    result = re.sub(matcher, "", result)
    print result

  if result == string:
    return None
  else:
    return result

def extract_meta_data(filepath):
  filename = os.path.basename(filepath)

  extension_pattern = "\.(.*)$"
  extension = extract_first(extension_pattern, filename)
  if extension is None:
    raise RuntimeError("Can't find file extension for filename: {}".format(filename))

  episode_pattern = "_E?(\d+)_"
  episode = extract_first(episode_pattern, filename)
  if episode is None:
    raise RuntimeError("Can't find episode number in filename: {}".format(filename))

  anime = filter_out(filename,
                     "(\[\w*\])",
                     extension_pattern,
                     episode_pattern,
                     #"[Rr]emastered",
                     "^[_-]*",
                     "[_-]{2,}")

  return {'anime': anime,
          'episode': episode,
          'extension': extension}


def rename(filename, dest_folder):
  if not os.path.exists(filename):
    raise RuntimeError("file {} does not exist".format(filename))
  if dest_folder and (not os.path.exists(dest_folder)):
    raise RuntimeError("destination folder {} does not exist".format(dest_folder))


if __name__ == "__main__":
  dp.hello()
  args = docopt(__doc__)
  try:
    rename(args['<input_file>'], args['<dest_folder>'])
  except RuntimeError as e:
    print "RuntimeError:", e
