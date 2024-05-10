import random

def caesar(inp: str, shift: int) -> str:
    shift = shift % 26
    def encrypt_char(char: str, shift: int) -> str:
        if char < 'A':
            return char
        elif char <= 'Z':
            base_alphabet: int = ord('A')
            base_char: int = ord(char) - ord('A')
        elif char < 'a':
            return char
        elif char <= 'z':
            base_alphabet: int = ord('a')
            base_char: int = ord(char) - ord('a')
        else:
            return char
        return chr(base_alphabet + (base_char + shift) % 26)
    return ''.join([encrypt_char(c, shift) for c in inp])

def permute_sentence(inp: str) -> str:
    return ''.join(random.sample(list(inp), len(inp)))

def permute_words(inp: str) -> str:
    return ' '.join([permute_sentence(word) for word in inp.split()])