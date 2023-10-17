# Task 1
def encrypt_by_add_mod(text,key):
    encrypted_text = []
    for char in text:
        encrypted_text.append(chr((ord(char) + key) % 256))
        
    return ''.join(encrypted_text)


# Task 2
def encrypt_xor_with_changing_key_by_prev_cipher(text, initial_key, mode):
    result = []
    key = initial_key
    for char in text:
        if mode == 'encrypt':
            cipher_byte = ord(char) ^ key
            result.append(cipher_byte)
            key = cipher_byte
        elif mode == 'decrypt':
            plain_byte = ord(char) ^ key
            result.append(plain_byte)
            key = ord(char)
    return ''.join([chr(byte) for byte in result])

# Task 3

def chunk_string(string, chunkSize):
    return [string[i::chunkSize] for i in range(chunkSize)]

def reverse_chunk_string(chunks):
    result = []
    for i in range(len(chunks[0])):
        for chunk in chunks:
            if i < len(chunk):
                result.append(chunk[i])

    return ''.join(result)

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(text : str, key_list : list, mode):
    encrypted_chunk = []
    for idx,char in enumerate(chunk_string(text, len(key_list))):
        encrypted_chunk.append(encrypt_xor_with_changing_key_by_prev_cipher(char, key_list[idx], mode))
        
    return reverse_chunk_string(encrypted_chunk)