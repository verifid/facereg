#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
import face_recognition
import pickle

from imutils import paths

datasets_path = os.getcwd() + '/datasets'
encodings_path = os.path.dirname(os.path.realpath(__file__)) + '/encodings.pickle'

def encode_faces(datasets=datasets_path, encodings=encodings_path, detection_method='cnn'):
    """Encodes (128-d vectors) given images on datasets.
    Args:
      datasets (str):
        Directory path of datasets that contains images.
      encodings (str):
        Directory path of encoding file.
      detection_method (str):
        Face detection method. Options: `cnn` or `hog`.
    """

    known_encodings = []
    known_names = []
    image_paths = list(paths.list_images(datasets))
    for (i, imagePath) in enumerate(image_paths):
        print("[INFO] processing image {}/{}".format(i + 1, len(image_paths)))
        name = imagePath.split(os.path.sep)[-2]
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect the (x, y) coordinates of the bounding boxes
        boxes = face_recognition.face_locations(rgb, model=detection_method)
        # compute the facial embedding for the face
        face_encodings = face_recognition.face_encodings(rgb, boxes)
        # loop over the encodings
        for face_encode in face_encodings:
            known_encodings.append(face_encode)
            known_names.append(name)
    # save facial encodings and names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": known_encodings, "names": known_names}
    f = open(encodings, "wb")
    f.write(pickle.dumps(data))
    f.close()
