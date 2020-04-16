import sys


class Caesar():
    def __init__(self, k=0, array=None):
        """Caesar init
        Params:
            k (int): number of places to move the alphabet
            array (str): message to encode
        """
        self.array = list(array)
        self.k = k % 26
        self.code = self.encode()

    def displacement(self, _c):
        """function to get an encoded char
        Params:
            _c (str): char to change
        Return
            str: encoded char
        """
        if not _c.isalpha():
            return chr(ord(_c))
        _n = 65 if _c.isupper() else 97
        return chr(((ord(_c) + self.k) % _n) % 26 + _n)

    def encode(self):
        """get the encode message
        Return:
            str: encoded message
        """
        array2 = list(map(self.displacement, self.array))
        return "".join(map(str, array2))


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        sys.exit("Usage: python3 caesar.py k")
    else:
        k = int(sys.argv[1])
        _str = input("plaintext: ")
        c = Caesar(k, _str)
        sys.exit("ciphertext: {}".format(c.code))
