import uuid
from Crypto.Cipher import AES
import base64
import random
import string
import os

BLOCK_SIZE = 16
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

def create_key():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(BLOCK_SIZE))

def encrypt(text,key):
    # cipher = AES.new(key)
    # encoded = EncodeAES(cipher, text)
    return text
    # pass
def decrypt(enc_text,key):
    # cipher = AES.new(key)
    # decoded = DecodeAES(cipher, enc_text)
    return enc_text
    # pass
