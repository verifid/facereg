#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import face_recognition
import pickle
import cv2

from facereg import face_encoder

datasets_path = os.getcwd() + '/datasets'
encodings_path = os.path.abspath('facereg/encodings.pickle')
detection_method = 'cnn'

def recognize(image,
              datasets=datasets_path,
              encodings=encodings_path,
              detection_method=detection_method):
    """Recognize face from given image path.
    Args:
      image (str):
        Image path from file system.
      datasets (str):
        Datasets path from file system.
      encodings (str):
        Encodings path from file system.
      detection_method (str):
        Face detection method. Options: `cnn` or `hog`.
    Returns:
      names (list):
        List of names.
    """

    # encode faces
    face_encoder.encode_faces(datasets=datasets_path, encodings=encodings_path, detection_method=detection_method)
    # load the known faces and embeddings
    print('[INFO] loading encodings...')
    with open(encodings_path, 'rb') as handle:
        data = pickle.load(handle)
    # load the input image and convert it from BGR to RGB
    image = cv2.imread(image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # bounding boxes corresponding to each face in the input image
    print('[INFO] recognizing faces...')
    boxes = face_recognition.face_locations(rgb, model=detection_method)
    encodings = face_recognition.face_encodings(rgb, boxes)
    # initialize the list of names for each face detected
    names = []
    # facial embeddings
    for encoding in encodings:
        # compare input image to our known encodings
        matches = face_recognition.compare_faces(data['encodings'],
            encoding)
        name = 'Unknown'

        if True in matches:
            # matched faces indexes
            matched_idxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # maintain a count for each recognized face
            for i in matched_idxs:
                name = data['names'][i]
                counts[name] = counts.get(name, 0) + 1

            # find the name with largest vote
            name = max(counts, key=counts.get)
        # update the list of names
        names.append(name)
    return names
