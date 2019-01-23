#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest

from facereg import face_encoder

class FaceEncoderTest(unittest.TestCase):
    
    def test_encode_faces(self):
        image_paths = face_encoder.encode_faces()
        self.assertEqual(len(image_paths), 3)
