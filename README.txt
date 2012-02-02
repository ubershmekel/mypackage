mypackage - an empty package to be used as a template
============================================


Installation
------------------------------------------------------------
Use pip or easy_install:
    % pip install mypackage
or
    % easy_install mypackage

Or download the source, extract the package then run:

    % python setup.py install


Building
------------------------------------------------------------
The distribution itself may be built as a zip archive (.zip)
and gzipped tarball (.tar.gz) using:

    % python setup.py sdist --formats=gztar,zip

This will place the distribution files in directory dist.  It uses the
MANIFEST.in file to determine which additional files on top of those
ending in .py to include (there's an include syntax for patterns). 
This package includes everything.  


Uploading to PyPI
------------------------------------------------------------
After making sure your author and maintainer information is ok and registered
with PyPI, you can upload the package for the world to download and use.

    % python setup.py sdist upload


Running Unit Tests
------------------------------------------------------------

The unit tests are based on the python module unnittest.  They are
located in the folder "test" and may be run with:

   % python runtests.py

