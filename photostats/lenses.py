"""Create a graphs relating to lens usage on a directory of photos."""

from exif import Image
import os
import re


#directory = "/media/Photos/My Photos 2005 and on/2020/03-Mar-2020/Rebel T6s/Scarlett 8 year old birthday portraits"
directory = "/media/Photos/My Photos 2005 and on/2020/03-Mar-2020/Pixel"

def get_photos(directory: str) -> list:
    """Get photos from a directory.

    :param directory: a directory containing photos
    :returns: A list containing photo files with complete path
    """
    directory_files: list = os.scandir(path=directory)
    regex = re.compile('jpg$')  # needs to be generalized for all possible photo extensions
    photos: list = []
    for file in directory_files:
        if regex.search(file.name) and file.is_file():
            photos.append(file.path)
    return photos


def get_lens_make_model(photo_list: list) -> dict:
    """Obtain lens make and model for each photo passed in.

    :param photo_list: A list of photo files.
    :returns: A Counter dictionary, counting the makes/models of lenses.
    """
    for image in photo_list:
        print(image)
        with open(image, 'rb') as image_file:
            this_image = Image(image_file)
            print(dir(this_image))



def main():
    photos = get_photos(directory)
    get_lens_make_model(photos)


if __name__ == '__main__':
    main()

