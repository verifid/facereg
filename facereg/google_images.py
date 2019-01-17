#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from google_images_download import google_images_download

output_directory = os.getcwd() + '/datasets'

def download(keywords, type='face', limit=20, output_directory=output_directory):
    """Download images from Google with given parameters.
    Args:
      keywords (str):
        Keywords to download images.
      type (str):
        Denotes the type of image to be downloaded. Default `face`.
      limit (int):
        Maximum number of images to be downloaded. Default `20` and max `100`.
      output_directory (str):
        Directory name in which the images are downloaded.
    Returns:
      paths, output_directory (dictionary, str):
        Image paths and directory that has downloaded images.
    """

    downloader = google_images_download.googleimagesdownload()
    arguments = {'keywords': keywords, 'limit': limit, 
                 'output_directory': output_directory, 'print_urls': True}
    paths = downloader.download(arguments)
    return (paths, output_directory)
