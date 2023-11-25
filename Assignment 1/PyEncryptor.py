
import os

# Substitution: ceasar ez
# Transcription: playfair
encryptedNm = "encyptedfile"

textFile = r'/home/ant/UNI/1DV700/Assignment 1/textFile.txt'
outputFile = f'/home/ant/UNI/1DV700/Assignment 1/{encryptedNm}.txt'


# simple playfair cipher
# setting all necessary functions under the same one for readability
def palyfair_encryptor(plain_text, secret_key):
    def generate_matrix(key):
        pass

    def find_coordinates(char, matrix):
        pass

    def encrypt_pair(pair, matrix):
        pass

    pass


# simple ceasar cipher
def caesar_encryption(plain_text, secret_key, output_file):
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
