#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from facereg import google_images

class DownloadGoogleImagesTest(unittest.TestCase):

    def test_download_images(self):
        paths, errors = google_images.download('michael jordan', limit=3)
        self.assertEqual(len(paths['michael jordan']), 3)
