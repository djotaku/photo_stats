=====
Usage
=====

If you installed to a virtual environment, activate the virtual environment and
run the following to run all statistics against a directory (in the example we'll
call it DIRECTORY) and put the resulting graphs in another directory (In the
example we'll call it GRAPHS)

.. code-block:: Bash

    source ./bin/activate
    python -m photostats -p DIRECTORY -g GRAPHS

Be patient if you have a lot of photos. It takes minutes. Go grab a cup of tea or coffee.
When if is done, you'll have output the looks like the following:

.. code-block:: Bash

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

Then head over to the directory specified by GRAPHS and you'll have graphs in there.