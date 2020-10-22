#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from facereg import google_images


class DownloadGoogleImagesTest(unittest.TestCase):
    def test_download_images(self):
        paths, _ = google_images.download("michael jordan", limit=1)
        # self.assertEqual(len(paths['michael jordan']), 1)


if __name__ == "__main__":
    images_tests = DownloadGoogleImagesTest()
    images_tests.test_download_images()
