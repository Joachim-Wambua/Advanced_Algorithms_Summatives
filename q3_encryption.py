# Q3 - Encrypting User Data using multidimensional matrices
# Author: Joachim Wambua
from itertools import chain


# Function to handle text encryption
def text_encryptor(text, key):
    # Variables to check current index & encrypted texts
    current_key = 0
    encrypted_txt = ''
    # Evaluate Length of original text
    text_len = len(text)
    # Create (key) no of rows
    encryption_matrix = [[] for x in range(key)]

    for index in range(text_len):
        # If the currently occupied key is < than max key value
        if current_key < key:
            # On current key append a text symbol
            encryption_matrix[current_key].append(text[index])
            # Increase current key by one
            current_key = current_key + 1
        # If current key is at max key value
        elif current_key == key:
            # Set current key back to 0
            current_key = 0
            # append letter to encryption table
            encryption_matrix[current_key].append(text[index])
            # Increase current key by one
            current_key = current_key + 1
    # Join strings from the different matrix keys
    encrypted_txt = ''.join(chain(*encryption_matrix))
    # Returns final encrypted text
    return encrypted_txt


def text_decryptor(encrypted_text, key):
    current_key = 0
    decrypted_text = ''
    decryption_matrix = [[] for x in range(key)]
    # Evaluate encrypted text length
    n = len(encrypted_text)
    for i in range(n):
        if current_key < key & i % key == 0:
            decryption_matrix[current_key].append(encrypted_text[i])
        else:
            decryption_matrix[current_key].append(encrypted_text[i])
    decrypted_txt = ''.join(chain(*decryption_matrix))
    return decrypted_text


if __name__ == '__main__':
    result = text_encryptor('plain text', 2)
    result_a = text_encryptor('plain text', 3)
    result_one = text_encryptor('Joachim Wambua', 2)
    result_one_a = text_encryptor('Joachim Wambua', 3)
    result_one_b = text_decryptor('pantxli et', 2)
    # result_one_a = text_encryptor('Joachim Wambua', 3)
    print(result)
    print(result_a)
    print(result_one)
    print(result_one_a)
    print(result_one_b)
