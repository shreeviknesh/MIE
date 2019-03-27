from MIE import MIE_PDF, MIE

m = MIE_PDF('data/test.pdf')
m.getImages()
m.encryptImages()
m.decryptImages()
