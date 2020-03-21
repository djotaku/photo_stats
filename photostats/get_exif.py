"""Get EXIF data from a directory of photos"""

import itertools
from pyexiv2 import Image
import os
import re


def scan_tree(directory: str):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry


def get_photos(this_directory: str) -> list:
    """Get photos from a directory.

    :param this_directory: a directory containing photos
    :returns: A list containing photo files with complete path
    """
    directory_files: list = os.scandir(path=this_directory)
    #directories_list = []
    #for root, directories, files in os.walk('/media/Photos/My Photos 2005 and on/2020/03-Mar-2020/'):
    #    directories_list.append(directories)
    #directory_files = list(itertools.chain.from_iterable(directories_list))
    regex = re.compile('CR2$')  # needs to be generalized for all possible photo extensions
    photos: list = []
    for file in directory_files:
        if regex.search(file.name) and file.is_file():
            photos.append(file.path)
    return photos


def get_exif(photo_list: list) -> list:
    """Obtain exif data for each photo from the list.

    :param photo_list: A list of photos from a directory
    :returns: A list of exif dictionaries from photos
    """
    exif_list = []
    for image in photo_list:
        this_image = Image(image)
        this_image_exif = this_image.read_exif()
        exif_list.append(this_image_exif)
    return exif_list
