from typing import Dict

def Nomenclator(permutation: Dict[str, str], word_replacements: Dict[str, str], message: str) -> str:
    encrypted_text = ''.join([permutation.get(ch, ch) for ch in message])
    
    for word, substitute in word_replacements.items():
        parts = encrypted_text.split(" " + word + " ")
        new_parts: List[str] = []
        prev_part = parts[0]
        for part in parts[1:]:
            if not (prev_part and part):
                new_parts.append(prev_part)
                new_parts.append(word)
                prev_part = part
            else:
                new_parts.append(prev_part)
                new_parts.append(substitute)
                prev_part = part

        new_parts.append(prev_part)
        encrypted_text = " ".join(new_parts)
        encrypted_text = encrypted_text.replace(word, substitute)

    return encrypted_text

if __name__ == "__main__":
    print("Enter the permutation for each letter (e.g. a:z). Press Enter twice to end input.")
    permutation: Dict[str, str] = {}
    while True:
        pair = input("Permutation: ")
        if not pair:
            break
        key, value = pair.split(':')
        permutation[key.strip()] = value.strip()

    print("\nEnter up to 5 word replacements (e.g. the:2). Press Enter twice to end input.")
    word_replacements: Dict[str, str] = {}
    for _ in range(5):
        replacement = input("Word Replacement: ")
        if not replacement:
            break
        word, substitute = replacement.split(':')
        word_replacements[word.strip()] = substitute.strip()

    message: str = input("\nEnter the message to be encrypted: ")

    encrypted_message = Nomenclator(permutation, word_replacements, message)
    print("\nEncrypted Message:", encrypted_message)


