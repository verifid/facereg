#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import imutils
import cv2

from facereg import recognize_faces


class RecognizeFacesTest(unittest.TestCase):
    def test_recognize(self):
        file_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = file_dir + "/resources/michael_jordan.jpeg"
        image = cv2.imread(image_path)
        resized = imutils.resize(image, width=100)
        resized_image_path = file_dir + "/resources/resized_image.jpeg"
        cv2.imwrite(resized_image_path, resized)
        datasets = os.path.abspath(os.path.join("datasets/michael jordan", os.pardir))
        names = recognize_faces.recognize(image_path, datasets=datasets)
        self.assertEqual(len(names), 1)
        self.assertEqual(names[0], "michael jordan")


if __name__ == "__main__":
    recognition_tests = RecognizeFacesTest()
    recognition_tests.test_recognize()
