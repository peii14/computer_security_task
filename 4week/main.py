# letter frequency from https://github.com/Vazno/english-words#get-the-letter-frequency-by-running-find_frequencypy

def score_english_text(text):
    english_letter_freq ={
    "e": 10.984012884727973,
    "i": 8.954280134924268,
    "a": 8.322183512716474,
    "s": 8.267897651036094,
    "o": 7.1027394245509345,
    "r": 7.020600703586417,
    "n": 6.871444737513424,
    "t": 6.585556553136487,
    "l": 5.348742882375743,
    "c": 4.197972539021217,
    "u": 3.4867188953134782,
    "d": 3.248135609584791,
    "p": 3.206320824236389,
    "m": 3.0029973178903386,
    "h": 2.725509953433427,
    "g": 2.4479515961321203,
    "y": 1.8032655761850245,
    "b": 1.788783035928532,
    "f": 1.1381809456152217,
    "v": 0.8834586199275021,
    "k": 0.8482225048263302,
    "w": 0.7037993950463086,
    "z": 0.4429953490221209,
    "x": 0.29400503291938196,
    "q": 0.16456141330661478,
    "j": 0.1596629070433894,
    ' ': 0.13000
    }

    return sum([english_letter_freq.get(char, 0) for char in text.lower()])

def decrypt_single_byte_xor(encrypted_text):
    encrypted_bytes = bytes.fromhex(encrypted_text)
    
    possible_texts = []
    for key in range(256):
        decrypted_text = ''.join([chr(b ^ key) for b in encrypted_bytes])
        possible_texts.append((key, decrypted_text))

    text = max(possible_texts, key=lambda x: score_english_text(x[1]))
    
    return text[1]

