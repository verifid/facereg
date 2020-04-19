# facereg

[![Build Status](https://github.com/verifid/facereg/workflows/facereg%20ci/badge.svg)](https://github.com/verifid/facereg/actions)
[![pypi](https://img.shields.io/pypi/v/facereg.svg)](https://pypi.python.org/pypi/facereg/)
[![pyversions](https://img.shields.io/pypi/pyversions/facereg.svg)](https://pypi.org/project/facereg)
[![codecov](https://codecov.io/gh/verifid/facereg/branch/master/graph/badge.svg)](https://codecov.io/gh/verifid/facereg)


**Documentation**: <a href="https://facereg.verifid.app" target="_blank">https://facereg.verifid.app</a>

**Source Code**: <a href="https://github.com/verifid/facereg" target="_blank">https://github.com/verifid/facereg</a>

**facereg** is a module for face recognition with OpenCV and Deep Learning.

For now it can be used for just images. It is easy to use with a handy feature 
which downloads images from Google for you with given keywords to create dataset/s.

Uses two different technics **CNN** and **HoG** for recognition based on <a href="https://github.com/verifid/facereg" target="_blank">dlib's</a> face recognition system with using <a ref="https://github.com/ageitgey/face_recognition">face_recognition</a>. **facereg** has totally three different layers and only recognizer has connection on encoder.

CLI is available that you can download images from Google and do face recognition.
