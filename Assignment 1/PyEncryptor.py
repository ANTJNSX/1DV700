# backslashes in file path
# makes the program not able to open in windows directories.

# Substitution: ceasar ez
# Transposition : atbash

# Simple atbash encryptor, inverting the letters of the words
# Atbash is symmetric, so decryption is the same as encryption
def atbash(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(ord('z') - (ord(char) - ord('a')))
            else:
                encrypted_text += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            encrypted_text += char

    return encrypted_text


def atbash_encrypt_file(input_file, output_file):
    try:  # catch block for file problems
        with open(input_file, 'r') as file:
            plaintext = file.read()
            encrypted_text = atbash(plaintext)

        with open(output_file, 'w') as file:
            file.write(encrypted_text)

    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def atbash_decrypt_file(input_file, output_file):
    try:  # catch block for file problems
        with open(input_file, 'r') as file:
            encrypted_text = file.read()
            decrypted_text = atbash(encrypted_text)

        with open(output_file, 'w') as file:
            file.write(decrypted_text)
    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# simple ceasar encryptor, uses a given key to shift the letters forwards
def caesar_encryptor(plain_text, secret_key, output_file):
    try:  # catch block for file problems
        with open(plain_text, "r", encoding="utf-8") as plain_text:
            shift = secret_key
            result = []

            for line in plain_text:
                line_res = []
                line = line.split(" ")

                for word in line:
                    word = word.lower()
                    cr_word = ""

                    # shift the characters
                    for ch in word:
                        if ch.isalpha():
                            new_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
                            cr_word += new_ch
                        else:
                            cr_word += ch

                    line_res.append(cr_word)

                result.append(" ".join(line_res))

            with open(output_file, "w", encoding="utf-8") as file:
                for line in result:
                    file.write(line)

            return 'File encrypted under:', output_file

    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# simple ceasar encryptor, uses a given key to shift the letters forwards
def caesar_decryptor(encrypted_text, secret_key, output_file):
    try:  # catch block for file problems
        with open(encrypted_text, "r", encoding="utf-8") as encrypted_text:

            shift = secret_key
            result = []

            for line in encrypted_text:
                line_res = []
                line = line.split(" ")

                for word in line:
                    word = word.lower()
                    decr_word = ""

                    # shift the characters in the opposite direction
                    for ch in word:
                        if ch.isalpha():
                            new_ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
                            decr_word += new_ch
                        else:
                            decr_word += ch

                    line_res.append(decr_word)

                result.append(" ".join(line_res))

            with open(output_file, "w", encoding="utf-8") as file:
                for line in result:
                    file.write(line)

            return 'File decrypted under:', output_file

    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# main loop for multiple uses from inputs
while True:
    cipher_type = int(input("\nPick a cipher:\n1. Encrypt: Atbash\n2. Decrypt: Atbash\n3. Encrypt: Ceasar\n4. Decrypt: Ceasar\n\n"))

    match cipher_type:
        case 1:
            text_file = str(input("\nName of file to encrypt: "))
            output_file = "encrypted_" + text_file
            atbash_encrypt_file(text_file, output_file)

        case 2:
            text_file = str(input("\nName of file to decrypt: "))
            output_file = text_file
            atbash_encrypt_file(text_file, output_file)

        case 3:
            text_file = str(input("\nName of file to encrypt: "))
            output_file = "encrypted_" + text_file
            shift_key = int(input("\nShift key(1-25): "))
            caesar_encryptor(text_file, shift_key, output_file)

        case 4:
            text_file = str(input("\nName of file to decrypt: "))
            output_file = "decrypted_" + text_file
            shift_key = int(input("\nShift key(1-25): "))
            caesar_decryptor(text_file, shift_key, output_file)
