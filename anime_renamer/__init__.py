import os.path
import os
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
  for matcher in matchers:
    result = re.sub(matcher, "", result)

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
                     "('\w*')",
                     extension_pattern,
                     episode_pattern,
                     "[Rr]emastered",
                     "^[_-]*",
                     "[_-]*$")

  if anime is None:
    raise RuntimeError("Can't extract anime name form filename: {}".format(filename))

  return {'anime': anime,
          'episode': episode,
          'extension': extension}


def filename_from_metadata(meta_data):
  return "{anime}/{anime}-E{episode}.{extension}".format(**meta_data)


def rename(filepath, dest_folder):
  if not os.path.exists(filepath):
    raise RuntimeError("file {} does not exist".format(filepath))
  if dest_folder and (not os.path.exists(dest_folder)):
    raise RuntimeError("destination folder {} does not exist".format(dest_folder))

  if dest_folder is None:
    dest_folder = os.path.dirname(filepath)

  dest_filename = filename_from_metadata(extract_meta_data(filepath))
  dest_path = os.path.join(dest_folder, dest_filename)
  print "{} -> {}".format(filepath, dest_path)
  #os.rename(filepath, dest_path)

