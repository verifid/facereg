#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from facereg import (
    google_images,
    recognize_faces
)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='CLI - face recognition from identity cards with OpenCV and Deep Learning.')
    parser.add_argument('-d', '--download', type=str, help='Keyword to download images from Google')
    parser.add_argument('-l', '--limit', type=int, default=3, help='Number of image is going to be downloaded from Google, max 20')
    parser.add_argument('-i', '--image', type=str, help='Directory path of your image for recognition')
    args = parser.parse_args()

    if len(sys.argv) < 2:
        print('Specify a key to use')
        sys.exit(1)

    # Optional bash tab completion support
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    args = parser.parse_args()
    if args.download != None:
        google_images.download(args.download, limit=args.limit)
    if args.image != None:
        print(recognize_faces.recognize(args.image))
