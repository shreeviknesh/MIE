# MIE
An image encryption algorithm that makes use of GF(2<sup>8</sup>) modular arithmetic.

### About the algorithm-
The MIE algorithm makes use of 2<sup>8</sup> modular arithmetic. So the encryption and decryption of the image file requires only one function.

### Prerequisites-
The MIE module uses opencv-python (cv2) package. So please make sure it is installed before trying to use the MIE module.
Also install: [ImageMagick](http://www.imagemagick.org/script/download.php) and [GhostScript](https://www.ghostscript.com/download/gsdnld.html)

### Algorithm-
1. Read the image file and convert it to a list of pixels.
2. For every pixel of the image, find the Modular Multiplicative Inverse of the RGB values and update it in the array.
3. Save the image using the new pixel values.
