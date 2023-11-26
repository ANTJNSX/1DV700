# Small script to shift the last character of each word in a wordlist
# to test the hashSets reaction to small changes in large quantitys of data

def shift_last_character(word):
    if len(word) > 0:
        last_char = word[-1]
        shifted_char = chr((ord(last_char) + 1) % 256)
        return word[:-1] + shifted_char
    return word


def shift_last_character_in_file(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as infile:
        lines = infile.readlines()

    shifted_lines = [shift_last_character(line.strip()) + '\n' for line in lines]

    with open(output_file, 'w', encoding="utf-8") as outfile:
        outfile.writelines(shifted_lines)


# Example usage:
input_filename = r'C:\Users\antom\Documents\UNI\1DV700\Assignment 1\hashing\words1.txt'
output_filename = r'C:\Users\antom\Documents\UNI\1DV700\Assignment 1\hashing\words1_shift.txt'
shift_last_character_in_file(input_filename, output_filename)
