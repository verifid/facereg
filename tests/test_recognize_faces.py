#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
import os

from facereg import recognize_faces

class RecognizeFacesTest(unittest.TestCase):

    def test_recognize(self):
        image_path = os.path.dirname(os.path.realpath(__file__)) + '/resources/michael_jordan.jpeg'
        names = recognize_faces.recognize(image_path)
        self.assertEqual(len(names), 1)
