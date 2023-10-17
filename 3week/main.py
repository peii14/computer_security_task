# concepts of base64 conversion from https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
# tutorial padding (both r and l padding) from https://www.w3schools.com/python/ref_string_ljust.asp

def hex2base64(hex_str: str) -> str:
    b64_tabel = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64_str = ""
    bin_str = bin(int(hex_str, 16))[2:]
    bin_str = bin_str.rjust(len(hex_str) * 4, '0')
    
    for i in range(0, len(bin_str), 6):
        bits = bin_str[i:i+6]
        if len(bits) < 6:
            bits = bits.ljust(6, '0')
        b64_str += b64_tabel[int(bits, 2)]
    
    b64_str += '=' * ((4 - len(b64_str) % 4) % 4)
    
    return b64_str

