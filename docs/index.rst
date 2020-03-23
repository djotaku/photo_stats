.. photostats documentation master file, created by
   sphinx-quickstart on Sun Mar 22 16:07:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to photostats's documentation!
======================================

photostats is a program to generate statistics from a directory of photos. It will
recursively search lower directories. It will generate graphs of the data. For example:

.. image :: _static/images/lens_models.png

After installing with pip install photostats, you can get a feel for all the commands
by typing python -m photostats -h. Or read further in this documentation.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   modules/get_exif
   modules/lenses
   modules/utils/create_plot

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
