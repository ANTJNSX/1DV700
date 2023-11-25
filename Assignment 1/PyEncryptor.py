# backslashes in file path
# makes the program not able to open in windows directories.

# Substitution: ceasar ez
# Transcription: atbash

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
    try:
            
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
    try:
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
    try:
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
    try:
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

