# AES CBC decrypt https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
# AES
from Crypto.Cipher import AES


def decrypt_aes(cipher_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_decrypt = cipher.decrypt(cipher_text), AES.block_size
    return padded_decrypt[0]

# Bit permutation 
def bit_permutation(source, pattern):
    result = []
    for i in pattern:
        result.append(source[i-1])
    return ''.join(result)

# bit rotation
def left_shift_rot(bits,steps = 1):
    steps %= len(bits)
    return bits[steps:] + bits[:steps]

# PKCS#7 padding
def PKCS7_pad(text, block_size):
    pad_length = block_size - (len(text) % block_size)
    padding = chr(pad_length) * pad_length
    return text + padding