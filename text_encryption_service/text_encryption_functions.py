import text_cryptography_helpers


# STEP 2
# P is converted to ASCII code and then to its corresponding 8-bit binary value PB.

def convert_plaintext_to_8bit(plaintext) -> str: 

    # error handling for plaintext that is not a string
    if not str(plaintext): 
        raise Exception("The entered plaintext must be of type string")

    # convert the plaintext first into ASCII and then into 8bit
    plaintext_array = list(plaintext)
    ascii_array = []
    binary_array = []
    for letter in plaintext_array:
        ascii_array.append(ord(letter))
        binary_array.append(text_cryptography_helpers.convert_to_binary_8dig(ord(letter)))
    # print(binary_array)
    Pb = ''.join(binary_array)
    return Pb

# res = convert_plaintext_to_8bit(text_cryptography_helpers.plaintext)
# print(res)

def generate_DNA_sequence_from_key(key) -> str:
    Db = ''
    for letter in key:
        Db+= text_cryptography_helpers.dna_dict[letter]
    # print(f'Db: {Db}')
    return Db

res = generate_DNA_sequence_from_key(text_cryptography_helpers.key)
print(res)