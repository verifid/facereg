facereg
=======

.. image:: https://img.shields.io/pypi/v/facereg.svg
    :target: https://pypi.org/pypi/facereg/

.. image:: https://img.shields.io/pypi/pyversions/facereg.svg
    :target: https://pypi.org/project/facereg

.. image:: https://travis-ci.org/verifid/facereg.svg?branch=master
    :target: https://travis-ci.org/verifid/facereg

.. image:: https://codecov.io/gh/verifid/facereg/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/verifid/facereg

**facereg** is a module for face recognition with OpenCV and Deep Learning.

For now it can be used for just images. It is easy to use with a handy feature 
which downloads images from Google for you with given keywords to create dataset/s.

Uses two different technics **CNN** and **HoG** for recognition based on `dlib <http://dlib.net/>`_'s
face recognition system with using `face_recognition <https://github.com/ageitgey/face_recognition>`_.
**facereg** is totally three different layers and only recognizer has connection on encoder.

|image_layers|

Prerequisites
=============

* All dependencies are listed on ``requirements.txt`` and will be installed when you install with **pip**.

Installation
============

* Install module using ``pip``::

    $ pip install facereg


* Download the latest ``facereg`` library from: https://github.com/verifid/facereg and install module using ``pip``::

    $ pip install -e .

* Extract the source distribution and run::

    $ python setup.py build
    $ python setup.py install

.. |image_layers| image:: https://raw.githubusercontent.com/verifid/facereg/master/resources/layers.png

Usage
=====

* ``google_images``:

.. code:: python

    import os
    from facereg import google_images

    output_directory = os.getcwd() + '/datasets' # directory path where you want to save photos
    image_paths, output_directory = google_images.download('michael jordan', limit=3)

* ``face_encoder``:

.. code:: python

    import os
    from facereg import face_encoder

    datasets_path = os.getcwd() + '/datasets'
    encodings_path = os.path.dirname(os.path.realpath(__file__)) + '/encodings.pickle'
    # these are default values for this method
    face_encoder.encode_faces(datasets=datasets_path, encodings=encodings_path, detection_method='cnn')

* ``recognize_faces``:

.. code:: python

    from facereg import recognize_faces

    image_path = 'DIRECTORY PATH OF YOUR_IMAGE'
    names = recognize_faces.recognize(image_path)
    # returns found names from your datasets

CLI Usage
=========

* Download images

.. code:: python

    # -d: keyword, -l: limit
    python -m facereg -d 'michael jordan'
    python -m facereg -d 'michael jordan' -l 5

* Recognition

.. code:: python

    # -i: Directory path for image
    python -m facereg -i tests/resources/michael_jordan.jpeg
