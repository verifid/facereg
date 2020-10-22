#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from facereg import face_encoder


class FaceEncoderTest(unittest.TestCase):
    def test_encode_faces(self):
        pickle_cached_stamp = 0
        face_encoder.encode_faces()
        pickle_encoding_path = face_encoder.encodings_path
        stamp = os.stat(pickle_encoding_path).st_mtime
        self.assertNotEqual(pickle_cached_stamp, stamp)


if __name__ == "__main__":
    face_encoder_tests = FaceEncoderTest()
    face_encoder_tests.test_encode_faces()
