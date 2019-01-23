#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from imutils import paths

datasets_path = os.getcwd() + '/datasets'
encodings_path = os.path.dirname(os.path.realpath(__file__)) + '/encodings.pickle'

def encode_faces(datasets=datasets_path, encodings=encodings_path, detection_method='cnn'):
    image_paths = list(paths.list_images(datasets))
    return image_paths
