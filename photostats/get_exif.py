"""Get EXIF data from a directory of photos"""

from pyexiv2 import Image
import os
import re


def get_photos(this_directory: str) -> list:
    """Get photos from a directory.

    :param this_directory: a directory containing photos
    :returns: A list containing photo files with complete path
    """
    directory_files: list = os.scandir(path=this_directory)
    regex = re.compile('CR2$')  # needs to be generalized for all possible photo extensions
    photos: list = []
    for file in directory_files:
        if regex.search(file.name) and file.is_file():
            photos.append(file.path)
    return photos


def get_exif(photo_list: list) -> list:
    """Obtain exif data for each photo from the list.

    :param photo_list: A list of photos from a diretory
    :returns: A list of exif dictionaries from photos
    """
    exif_list = []
    for image in photo_list:
        this_image = Image(image)
        this_image_exif = this_image.read_exif()
        exif_list.append(this_image_exif)
    return exif_list
