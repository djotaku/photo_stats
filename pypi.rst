==========
PhotoStats
==========



.. image:: https://codecov.io/gh/djotaku/photo_stats/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/djotaku/photo_stats

.. image:: https://readthedocs.org/projects/photo-stats/badge/?version=latest
   :target: https://photo-stats.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

This is a Python package that will eventually have a bunch of utilities for running a variety of stats on
your photos based on EXIF data. By using exiv-based library, it can also read data
from RAW files.

Currently will print output to the commandline and produce a bar graph for each
 category.

usage: __main__.py [-h] [-p PATH] [-g GRAPHPATH]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to recursively search for photos
  -g GRAPHPATH, --graphpath GRAPHPATH
                        Path to save graphs generated by this program

It will produce output like:

Lens Model Count:

EF17-40mm f/4L USM : 18

EF28-105mm f/3.5-4.5 USM : 80

55-200mm : 60

35mm : 23

Focal Length Count:

17 mm : 14

20 mm : 4

28 mm : 3

35 mm : 23

55 mm : 12

60 mm : 10

63 mm : 5

64 mm : 3

65 mm : 4

70 mm : 41

75 mm : 2

82 mm : 1

90 mm : 1

98 mm : 7

105 mm : 17

200 mm : 34

Make-Model Count:

Canon Canon EOS Rebel T6s : 181

Google Pixel : 143

Motorola XT1096 : 96