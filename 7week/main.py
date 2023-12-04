# https://www.youtube.com/watch?v=vVtYYMU3koM
from Crypto.Cipher import AES


def decrypt_aes_ecb(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_decrypt = cipher.decrypt(cipher_text), AES.block_size
    return padded_decrypt[0]


def xor_byte_arrays(bytes_a, bytes_b):
    length = max(len(bytes_a), len(bytes_b))
    bytes_a = bytes_a.ljust(length, b'\x00')
    bytes_b = bytes_b.ljust(length, b'\x00')

    return bytes(byte_a ^ byte_b for byte_a, byte_b in zip(bytes_a, bytes_b))


def decrypt_aes_cbc_with_ecb(cipher_text, key, iv):
    block_size = 16
    cipher = AES.new(key, AES.MODE_ECB)
    plain_text = b''
    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i:i+block_size]
        if i == 0:
            plain_text += xor_byte_arrays(cipher.decrypt(block), iv)
        else:
            plain_text += xor_byte_arrays(cipher.decrypt(block),
                                          cipher_text[i-block_size:i])
    return plain_text


def encrypt_aes_cbc_with_ecb(plaintext, key, iv):

    padding_len = 16 - (len(plaintext) % 16)
    padded_text = plaintext + bytes([padding_len] * padding_len)

    cipher_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext = b''
    previous_block = iv

    for i in range(0, len(padded_text), 16):
        block_to_encrypt = bytes(x ^ y for x, y in zip(
            plaintext[i:i+16], previous_block))
        encrypted_block = cipher_ecb.encrypt(block_to_encrypt)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext
