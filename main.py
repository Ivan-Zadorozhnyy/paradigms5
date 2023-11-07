def caesar_shift(char, shift):
    if char.isalpha():
        shift = shift % 26
        ascii_offset = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    return char

def caesar_cipher(text, key, operation):



def caesar_encrypt(text, key):



def caesar_decrypt(text, key):


def read_file(path):


def write_file(path, text):


def process_file(read_path, write_path, key, operation):


def main():
    if __name__ == "__main__":
        main()