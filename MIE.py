import cv2
import numpy as np

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


