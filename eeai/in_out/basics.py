"""
Originally created at 11/28/20, for Python 3.x
"""

import re
import os
import os.path as osp



def create_dir(dir_path):
    """ Creates a directory (or nested directories) if they don't exist.
    """
    if not osp.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path


def files_in_subdirs(top_dir, search_pattern):
    join = osp.join
    regex = re.compile(search_pattern)
    for path, _, files in os.walk(top_dir):
        for name in files:
            full_name = join(path, name)
            if regex.search(full_name):
                yield full_name


def splitall(path):
    """
    Examples:
        splitall('a/b/c') -> ['a', 'b', 'c']
        splitall('/a/b/c/')  -> ['/', 'a', 'b', 'c', '']

    NOTE: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s16.html
    """
    allparts = []
    while 1:
        parts = osp.split(path)
        if parts[0] == path:    # Sentinel for absolute paths.
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # Sentinel for relative paths.
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


def trim_content_after_last_dot(s):
    """Example: if s = myfile.jpg.png, returns myfile.jpg
    """
    index = s[::-1].find('.') + 1
    s = s[:len(s) - index]
    return s