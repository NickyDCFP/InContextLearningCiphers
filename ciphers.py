def caesar(inp: str, shift: int) -> str:
    """
    Performs a caesar cipher on the input data with the specified shift.

    Parameters:
        inp:    The input string to be encrypted
        shift:  The shift for the Caesar cipher.

    Returns:    
        The encrypted string.
    """
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