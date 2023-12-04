import hashlib


# ------------------ REGION SHA256 ------------------
def sha256(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()
# ------------------ ENDREGION SHA256 ------------------


# ------------------ REGION authenticate ------------------

def authenticate(username, password):
    users = {
        # sha256('admin')
        'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
        # sha256('hello')
        'user': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
    }
    if username in users and users[username] == sha256(password):
        return True
    return False
# ------------------ ENDREGION authenticate ------------------


# ------------------ REGION hack sha256 fixed size ------------------


def generate_combinations(length):
    chars = 'abcdefghijklmnopqrstuvxyz'
    if length == 0:
        return ['']
    smaller_combinations = generate_combinations(length - 1)
    return [s + char for s in smaller_combinations for char in chars]


def hack_sha256_fixed_size(hash_value, password_length):
    for password in generate_combinations(password_length):
        if sha256(password) == hash_value:
            return password

    return None
# ------------------ ENDREGION hack sha256 fixed size ------------------

# ------------------ REGION hack sha256 ------------------


def hack_sha256(hash_value):
    for length in range(1, 11):
        result = hack_sha256_fixed_size(hash_value, length)
        if result is not None:
            return result
    return None

# ENDREGION hack sha256

# ------------------ REGION Longer example ------------------

# HASH: e06554818e902b4ba339f066967c0000da3fcda4fd7eb4ef89c124fa78bda419
# Answer: cryptography
# Method: Rainbow table attacks and list from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
# Short explaination: I create a list of the most common passwords and I hash them. Then create object with keys as the plain text password and the value as the hashed password. Then I compare the hash with the one target hash from the question.

# HASH: 8aa261cbc05ad6a49bea91521e51c8b979aa78215b8defd51fc0cebecc4d5c96
# Answer:romeo and juliet
# Method: Im using hashcat tools to crack the hash. In addition to that, I use most common password list from crack station (https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm).
# Short explaination: the command was "hashcat -m 1400 -a 0 -o cracked.txt hashes.txt crackstation.txt". the method 1400 that use sha256 hash algorithm. -a 0 means that I use a dictionary attack.then the result of the cracked hash will be saved in cracked.txt. the hashes.txt is the file that contain the hash that we want to crack. the crackstation.txt is the file that contain the list of the most common password.

# HASH: f2b826b18b9de86628dd9b798f3cb6cfd582fb7cee4ea68489387c0b19dc09c1
# Answer: vulnerable
# Method: Im using hashcat tools to crack the hash. In addition to that, I use most common password list from crack station (https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm).
# Short explaination: the command was "hashcat -m 1400 -a 0 -o cracked.txt hashes.txt crackstation.txt". the method 1400 that use sha256 hash algorithm. -a 0 means that I use a dictionary attack.then the result of the cracked hash will be saved in cracked.txt. the hashes.txt is the file that contain the hash that we want to crack. the crackstation.txt is the file that contain the list of the most common password.


# ------------------ ENDREGION Longer example ------------------

# ------------------ REGION Auth with pepper ------------------


def authenticate_with_pepper(username, password):
    pepper_prefix = 'this_can_help_to_confuse_the_attacker_'
    users_with_pepper = {
        'admin': {'passwordHash': '89e6b5ed137e3864d99ec9b421cf6f565d611f4c2b98e31a7d353d63aa748e9c'},
        'user': {'passwordHash': '6dc765830e675d5fa4a9afb248be09a0407f6353d44652fd9b36038884a76323'}
    }

    password_hash = sha256(pepper_prefix + password)

    return users_with_pepper.get(username, {}).get('passwordHash') == password_hash
# ------------------ ENDREGION Auth with pepper ------------------

# ------------------ REGION Auth with pepper and salt ------------------


def authenticate_with_pepper_and_salt(username, password):
    pepper_prefix = 'this_can_help_to_confuse_the_attacker_'
    users_with_pepper_and_salt = {
        'admin': {'passwordHash': 'd3eab7f4d6974f1db32b9cd9923fce9b434b28dc229b6582b845f1fca770d9f7', 'salt': "5294976873732394418"},
        'user': {'passwordHash': '976c73e0b408c89df3c1a12c3b0c45a6fee71bc1de5b47a88fae1a5e69ba6e28', 'salt': '1103733363818826232'}
    }

    user_data = users_with_pepper_and_salt.get(username)

    if not user_data:
        return False

    password_hash = sha256(pepper_prefix + password + user_data['salt'])

    return password_hash == user_data['passwordHash']


# ------------------ ENDREGION Auth with pepper and salt ------------------
