"""Create a graphs relating to lens usage on a directory of photos."""

from collections import Counter

from photostats import get_exif


def get_lens_make_model(exif_list: list) -> dict:
    """Obtain lens make and model for each photo passed in.

    :param exif_list: A list of photo files.
    :returns: A Counter dictionary, counting the makes/models of lenses.
    """
    lens_list = []
    for data in exif_list:
        lens_list.append((data.get("Exif.Photo.LensModel")))
    return Counter(lens_list)


def main():
    directory = "/media/Photos/My Photos 2005 and on/2020/"
    photos = get_exif.get_photos(directory)
    exif = get_exif.get_exif(photos)
    lens_count = get_lens_make_model(exif)
    print("Lens Model Count:")
    for lens, count in lens_count.items():
        print(f'{lens} : {count}')


if __name__ == '__main__':
    main()
