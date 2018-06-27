# stego-py

## Introduction

### What is Steganography?

> [Steganography](https://en.wikipedia.org/wiki/Steganography) is the practice of concealing a file, message, image, or video within another file, message, image, or video.


### What is stego-py?

stego-py is a custom python library which you can import to encrypt a image in another or to decrypt.

#### Encryption

Import stego-py to your python project.Use en_stego.hide().Give own file paths for the images you want to encrypt in ,

```
en_image = en_stego.hide([parent image path],[child image path])
```

find the encypted image in the dist folder.

#### Decryption

Use de_stego.show().Give you own file path for the image you want to decrypt in,

```
de_image = de_stego.show('./dist/en.png')
```

find the decrypted images in the dist folder.


## Prerequisites

### Installation - OpenCV 3 with python 3

### MacOS
https://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/

### Ubuntu
https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

### Windows
https://solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/
