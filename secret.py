import os
import binascii

secret_key = os.urandom(24)
print(binascii.hexlify(secret_key).decode())
