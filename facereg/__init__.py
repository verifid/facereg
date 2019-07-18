#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Face recognition from identity cards with OpenCV and Deep Learning."""

from __future__ import absolute_import

__author__       = 'Abdullah Selek'
__email__        = 'abdullahselek@gmail.com'
__copyright__    = 'Copyright (c) 2019 Abdullah Selek'
__license__      = 'MIT License'
__version__      = '0.2.1'
__url__          = 'https://github.com/verifid/facereg'
__download_url__ = 'https://pypi.org/project/facereg'
__description__  = 'Face recognition from identity cards with OpenCV and Deep Learning.'

from facereg import (
    google_images,
    face_encoder,
    recognize_faces
)
