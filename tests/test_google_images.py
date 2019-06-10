#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
import os

from facereg import google_images

class DownloadGoogleImagesTest(unittest.TestCase):

    def test_download_images(self):
        image_paths = google_images.download('michael jordan', limit=3)
        self.assertEqual(len(image_paths['michael jordan']), 3)
