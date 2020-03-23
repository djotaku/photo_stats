"""Test get_exif.py"""

from photostats import get_exif

file_paths = ['test_images/Canon/Canon EOS Rebel T1i.jpg', 'test_images/Canon/Canon EOS Rebel T6s.CR2',
              'test_images/Canon/Canon EOS Rebel XT.dng', 'test_images/Canon/Canon EOS Rebel XTi.dng',
              'test_images/Canon/Canon PowerShot A720 IS.jpg', 'test_images/Canon/Canon PowerShot S100.dng',
              'test_images/Canon/Canon PowerShot SD980 IS.jpg', 'test_images/Fujifilm/Fujifilm FinePix2650.JPG',
              'test_images/Fujifilm/Fujifilm FinePix A345.JPG', 'test_images/Fujifilm/Fujifilm Finepix S7000.JPG',
              'test_images/Apple/Apple iPhone 4S.JPG', 'test_images/Motorola/Motorola Droid2.jpg',
              'test_images/Motorola/Motorola XT1060.jpg', 'test_images/LG/LGE Nexus 5X.jpg',
              'test_images/LG/LG LG-VN250.jpg', 'test_images/LG/LG LG-VN271.jpg', 'test_images/Google/Google Pixel.jpg',
              'test_images/Kodak/Kodak DX3600.JPG', 'test_images/HTC/HTC ADR6350.jpg',
              'test_images/Nikon/Nikon D7200.jpg', 'test_images/Olympus/Olympus C4100Z.jpg',
              'test_images/Sony/Sony Cybershot.JPG', 'test_images/VTech/VTech Kidizoom camera.JPG']

test_directory = "test_images"


def test_scan_test():
    scan_tree = get_exif.scan_tree(test_directory)
    photos = []
    for file in scan_tree:
        photos.append(file.path)
    assert photos == file_paths


def test_get_photos():
    photo_list = get_exif.get_photos(test_directory)
    print(photo_list)
    assert photo_list == file_paths


def test_get_exif():
    exif = get_exif.get_exif(file_paths)
    assert exif[-1] == {'Exif.Image.ExifTag': '88', 'Exif.Image.Make': 'VTech', 'Exif.Image.Model': 'Kidizoom camera',
                        'Exif.Photo.DateTimeOriginal': '2018:12:26 19:18:50'}
