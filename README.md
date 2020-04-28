# MIE - Multiplicative Inverse Encryption
An image encryption algorithm that makes use of GF(2<sup>8</sup>) modular arithmetic. The function has been implemented in both C++ and Python.

About the algorithm
----
The MIE algorithm makes use of 2<sup>8</sup> modular arithmetic. Therefore, the encryption and decryption of the image file requires only one function.

i.e., `encrypt(encrypt(value)) = value`

Algorithm
----
1. Read the image file and convert it to an array of pixels.
2. For every pixel of the image, find the Modular Multiplicative Inverse of the RGB values and update it in the array.
3. Save the encrypted/decrypted pixel values as image

Prerequisites
----
#### C++
- The MIE-CPP module uses [https://github.com/nothings/stb](STB) libraries for reading and writing files.

#### Python
- The MIE-Python module uses [OpenCV](https://pypi.org/project/opencv-python/) and [Wand](https://pypi.org/project/Wand/) packages, so make sure it is installed before trying to use the MIE module.
- Also install: [ImageMagick](http://www.imagemagick.org/script/download.php) and [GhostScript](https://www.ghostscript.com/download/gsdnld.html) as they are prequisites for Wand.

Usage
----
#### C++
1. Compile and create an executable file of the program. 
    - Ex: `g++ encryptor.cpp -o encryptor.exe`
2. Pass the command line arguments for the executable file to perform encryption/decryption.
    - i.e., `encryptor.exe -E input.png output.png`
    - Usage: <FILE.exe> ((-E/-e/encrypt)/(-D/-d/decrypt)) <INPUT_FILENAME> <OUTPUT_FILENAME>

#### Python
1. Import the MIE.py file
2. Instantiate the MIE or MIE_PDF files depending on your requirement
3. MIE
    1. Load the image using the `MIE.loadImage()` method
    2. Encrypt/Decrypt the image using the `MIE.encrypt()` or `MIE.decrypt()` methods
    3. Save the image using the `MIE.saveImage()` method
4. MIE_PDF
    1. Load the PDF using the `MIE.getImages()` method
    2. Encrypt/Decrypt the PDF using the `MIE.encryptImages()` or `MIE.decryptImages()` methods
    3. The encrypted PDF will be saved automatically
5. End
