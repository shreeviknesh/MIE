from PIL import Image
class MIE:
    def __init__(self):
        #Creating an object for inverse class to be used
        from MultiplicativeInverse import MultiplicativeInverse
        self.Inverter = MultiplicativeInverse()
        self.loaded = False

    def loadImage(self, filename):
        #Opening the image
        self.image = Image.open(filename)
        self.pixels = list(self.image.getdata())
        self.loaded = True

    def saveImage(self, filename):
        newImage = Image.new(self.image.mode, self.image.size)
        newImage.putdata(self.pixels)
        newImage.save(filename, self.image.format)

    def showImage(self):
        newImage = Image.new(self.image.mode, self.image.size)
        newImage.putdata(self.pixels)
        newImage.show()

    def invertImage(self):
        assert self.loaded == True, 'Please load the image before trying to invert it!'

        for i in range(self.image.width):
            for j in range(self.image.height):
                index = i * self.image.height + j
                R, G, B = self.pixels[index]

                # R = self.Inverter.invert(R)
                # G = self.Inverter.invert(G)
                # B = self.Inverter.invert(B)

                R = 255 - R
                G = 255 - G
                B = 255 - B

                self.pixels[index] = (R, G, B)



