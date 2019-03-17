from PIL import Image
class MIE:
    def __init__(self):
        #Creating an object for inverse class to be used
        self.image = None
        self.pixels = []
        self.loaded = False

        import pickle
        with open('Multiplicative-Inverse', 'rb') as file:
            self.mulInv = pickle.load(file)

    def loadImage(self, filename):
        #Opening the image
        self.image = Image.open(filename)
        self.pixels = list(self.image.getdata())
        self.loaded = True

    def saveImage(self, filename):
        self.image.save(filename, self.image.format)

    def showImage(self):
        self.image.show()

    def invertImage(self):
        assert self.loaded == True, 'Please load the image before trying to invert it!'

        for index in range(self.image.width * self.image.height):
            R, G, B = self.pixels[index]

            r = self.mulInv[R]
            g = self.mulInv[G]
            b = self.mulInv[B]

            self.pixels[index] = (r, g, b)

        self.image.putdata(self.pixels)



