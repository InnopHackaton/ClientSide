#!/usr/bin/python3.6
import gnupg

class Encoder():
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='/home/hackathon/.gnupg')

    def encode(self, message):
        data = str(self.gpg.encrypt(message, "hack@hack.ru", always_trust=True, armor=True))
        result = data.replace("\n", "").replace("-----BEGIN PGP MESSAGE-----", "").replace("-----END PGP MESSAGE-----", "")
        return bytes(result, "utf-8")

class Decoder():
        pass
