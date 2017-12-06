import src.cryptopy.cipher.rijndael
from src.cryptopy.cipher.base import noPadding


class RijndaelCipher(object):
    def __init__(self, key, block_size=16):
        self.r = src.cryptopy.cipher.rijndael.Rijndael(key, padding=noPadding(), keySize=16, blockSize=block_size)

    def encrypt(self, plaintext):
        return self.r.encryptBlock(plaintext)

    def decrypt(self, ciphertext):
        return self.r.decryptBlock(ciphertext)
