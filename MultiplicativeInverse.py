def hex(decimal):
    #This function only takes 2 digits in hex
    decimal = decimal % 256

    values = '0123456789abcdef'
    h0 = values[decimal % 16]
    h1 = values[decimal // 16]

    return (h1 + h0)

def dec(hexadecimal):
    return int(hexadecimal, 16)

class MultiplicativeInverse:
    def __init__(self):
        #Loading the mul-inv one time
        import pickle
        with open('Multiplicative-Inverse', 'rb') as file:
            self.mulInv = pickle.load(file)

    def invert(self, decimal):
        hexadecimal = hex(decimal)
        value = self.mulInv[hexadecimal[0]][hexadecimal[1]]

        # print(decimal, hexadecimal, value, dec(value))
        return dec(value)

