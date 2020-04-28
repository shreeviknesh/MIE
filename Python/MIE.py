import cv2
from wand.image import Image as WandImage
from PIL import Image
import os

class MIE:
    def __init__(self):
        #Creating an object for inverse class to be used
        import pickle
        with open('Multiplicative-Inverse', 'rb') as file:
            self.mulInv = pickle.load(file)

    def loadImage(self, filename):
        #Opening the image
        self.image = cv2.imread(filename)

    def saveImage(self, filename):
        cv2.imwrite(filename, self.image)

    def showImage(self):
        cv2.imshow('image',self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def invertImage(self):
        def invert(num):
            return self.mulInv[num]

        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                for k in range(len(self.image[0][0])):
                    self.image[i][j][k] = invert(self.image[i][j][k])

    def encrypt(self):
        self.invertImage()

    def decrypt(self):
        self.invertImage()

class MIE_PDF():
    def __init__(self, filename, resolution = 100):
        self.filename = filename
        self.resolution = resolution
        self.pages = []

    def getImages(self):
        pdf = WandImage(filename = self.filename, resolution = self.resolution)
        pdfimage = pdf.convert('jpeg')

        PDF_NAME = self.filename[:-4]
        count = 0
        for img in pdfimage.sequence:
            count += 1
            page_filename = f'{PDF_NAME}_{count}.jpg'

            page = WandImage(image = img)
            page.save(filename = page_filename)

            image = Image.open(page_filename)
            new_filename = page_filename.replace('jpg', 'bmp')
            image.save(new_filename)

            os.remove(page_filename)
            self.pages.append(new_filename)

    def encryptImages(self):
        encryptor = MIE()
        enc_pages = []
        for image_input in self.pages:
            image_output = image_input.replace('.bmp', '_enc.bmp')

            encryptor.loadImage(image_input)
            encryptor.encrypt()
            encryptor.saveImage(image_output)

            enc_pages.append(image_output)

        self.enc_pages = enc_pages

    def decryptImages(self):
        decryptor = MIE()
        for image_input in self.enc_pages:
            image_output = image_input.replace('_enc.bmp', '_dec.bmp')

            decryptor.loadImage(image_input)
            decryptor.decrypt()
            decryptor.saveImage(image_output)
