#!/usr/bin/python3.6
import gnupg
from Crypto.Cipher import AES
import base64
import configparser


class Encoder():
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='/home/hackathon/.gnupg')

    def encode(self, message):
        data = str(self.gpg.encrypt(message, "hack@hack.ru", always_trust=True, armor=True))
        result = data.replace("\n", "").replace("-----BEGIN PGP MESSAGE-----", "").replace("-----END PGP MESSAGE-----",
                                                                                           "")
        return bytes(result, "utf-8")


class Decoder():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('configs/config.ini')

        self.secret_key = config["DEFAULT"]["SECRET_KEY"]
        self.cipher = AES.new(self.secret_key, AES.MODE_ECB)

    def decode(self, message):
        return self.cipher.decrypt(base64.b64decode(message)).decode("utf-8").lstrip()
