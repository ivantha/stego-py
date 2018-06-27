# stego-py
stego-py is a custom python library which you can import to encrypt a image in another or to decrypt.

## Introduction

### What is Steganography?

> [Steganography](https://en.wikipedia.org/wiki/Steganography) is the practice of concealing a file, message, image, or video within another file, message, image, or video.

Each pixel has three values (RGB), each RGB value is 8-bit(which can be represented in binary code) and the rightmost bits are least significant. So, if we change the rightmost bits it will have a small visual impact on the final image. This is the steganography key to hide an image inside another. Change the least significant bits from an image and include the most significant bits from the other image.

### Encryption

When encrypting a image in another image,what we do is merging the most significant bits from the parent image with the most significant bits from the child image.changing the least significant bits of the parent image will do no visble harm to the image.Now we have the child image encrypted in the parent.(child's most significant bits)

##### How to use?

Import stego-py to your python project.Use en_stego.hide().Give own file paths for the images you want to encrypt in ,

```
en_image = en_stego.hide([parent image path],[child image path])
```

find the encypted image in the dist folder.
For this your parent image should be same or larger in size than the child image.

### Decryption

When decrypting the image, we unmerge the last 4 bits (least significant) from the given image which belongs to the child image(most significant bits of thehidden image).Then concatenate 4 zero bits because we are working with 8 bit values.

##### How to use?

Use de_stego.show().Give you own file path for the image you want to decrypt in,

```
de_image = de_stego.show([image path])
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
