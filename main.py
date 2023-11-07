def caesar_shift(char, shift):
    if char.isalpha():
        shift = shift % 26
        ascii_offset = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    return char

def caesar_cipher(text, key, operation):
    shift = key if operation == 'encrypt' else -key
    return ''.join(caesar_shift(char, shift) for char in text)

def caesar_encrypt(text, key):


def caesar_decrypt(text, key):


def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        return None

def write_file(path, text):
    try:
        with open(path, 'w') as file:
            file.write(text)
        except Exception as e:
            print(f"erro while writing to the file: {e}")


def process_file(read_path, write_path, key, operation):


def main():
    if __name__ == "__main__":
        main()