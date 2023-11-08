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
    return caesar_cipher(text, key, 'encrypt')

def caesar_decrypt(text, key):
    return caesar_cipher(text, key, 'decrypt')

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
    text = read_file(read_path)
    if text is None:
        print("Failed to read from the input file.")
        return
    result_text = caesar_encrypt(text, key) if operation == 'encrypt' else caesar_decrypt(text, key)
    write_file(write_path, result_text)
    print(f"Text has been successfully {operation}ed to {write_path}.")

def main():
    while True:
        command = input("Choose your command\n1 - Encrypt text into the file\n2 - Decrypt text from the file\n")
        if command not in ['1', '2']:
            print("Invalid command. Please choose '1' for encrypt or '2' for decrypt.")
            continue

        key = int(input("Enter the key value: "))
        read_path = input("Enter the name of the input file: ").strip()
        write_path = input("Enter the name of the output file: ").strip()

        operation = 'encrypt' if command == '1' else 'decrypt'
        process_file(read_path, write_path, key, operation)
        print(f"Text has been successfully {operation}ed.")

if __name__ == "__main__":
     main()