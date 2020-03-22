import argparse

import get_exif  # type: ignore
import lenses  # type: ignore


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to recursively search for photos")
    return parser.parse_args()


def main():
    args = parse_args()
    photos = get_exif.get_photos(args.path)
    exif = get_exif.get_exif(photos)
    lenses.main(exif)


if __name__ == '__main__':
    main()
