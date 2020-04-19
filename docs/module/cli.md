# CLI

CLI helps you to download images from Google and do face recognition.

## Usage

First you need to install **facereg** either from PyPi or source. Then you can use sample
commands below.

Downloading images with default limit (which is 3)

```console
$ python -m facereg -d "michael jordan"
```

or with limiting number of files

```console
$ python -m facereg -d "michael jordan" -l 5
```

Face recognition by giving image path as a parameter

```console
$ python -m facereg -i IMAGE_PATH
```
