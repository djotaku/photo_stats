==========
PhotoStats
==========

This is a Python package with a bunch of utilities for running a variety of stats on
your photos based on EXIF data. By using exiv-based library, it can also read data
from RAW files.

Currently you can get lens stats by running:

python -m photostats.lenses

It will produce output like:

Lens Model Count:

EF17-40mm f/4L USM : 18

EF28-105mm f/3.5-4.5 USM : 80

Followed by a graph of the above data. Once you exit the graph window, you will get.

Focal Length Count:

17 mm : 14

20 mm : 4

63 mm : 5

98 mm : 7

70 mm : 41

105 mm : 17

28 mm : 3

82 mm : 1

65 mm : 4

75 mm : 2

Followed by another graph.