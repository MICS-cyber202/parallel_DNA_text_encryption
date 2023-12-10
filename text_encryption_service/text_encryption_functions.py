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

# STEP 3
# Now, a DNA sequence D is randomly chosen which will act as the key. D is converted to binary form using the conversion scheme 
# sited in Table 2 and named as DB.

def generate_DNA_sequence_from_key(key) -> str:
    print('key: ', key)
    Db = ''
    for letter in key:
        Db+= text_cryptography_helpers.dna_dict[letter]
    # print(f'Db: {Db}')
    return Db

# res = generate_DNA_sequence_from_key(text_cryptography_helpers.key)
# print(res)

# STEP 4
# Tf DB and PB are not of the same size then extra 0 s are added to the left side of DB or PB whichever is smaller in size. 
# The number of zeros added here is equal to the difference between the number of bits present in DB and PB.

# update method signature with types
def XOR_Pb_Db(Pb, Db) -> str:
    # Tf DB and PB are not of the same size then extra 0 s are added to the left side of DB or PB whichever is smaller in size. 
    # The number of zeros added here is equal to the difference between the number of bits present in DB and PB.            
    if len(Pb)<len(Db):
        Pb = '0'*(len(Db)-len(Pb))+Pb
    elif len(Pb)>len(Db):
        Db = '0'*(len(Pb)-len(Db))+Db

    # print(f'Pb: {Pb}')
    # print(f'Db: {Db}')

    # DB and PB are XOR-ed with each other and the resultant binary value is termed as R.
    R = ''
    for i in range(0,len(Pb)):
        R += text_cryptography_helpers.xor(Pb[i],Db[i])
    # print(f' R: {R}')
    return R

# res = XOR_Pb_Db(
#     '010110110011000000110000001110100011000000110000001110100011000000110011001011100011100100110011001100000101110100100000001011010010000001010011011100000110010101100001011010110110010101110010001000000011000100100000010011110110101101100001011110010010111000100000010100000110010101110010011001100110010101100011011101000010111000100000010010000110100100100000011101000110100001100101011100100110010100101110001000000101011101100101011011000110001101101111011011010110010100100000011101000110111100100000011011110111010101110010001000000110100101101110011101000110010101110010011101100110100101100101011101110010000001110111011010010111010001101000001000000101001001100001011011100110101001101001011101100010000001000010011010000110000101101001011100100010111000100000010010010110110100100000010101000110000101101110011011010110000101111001011010010010000001001110011000010110111001100100011000010110111000100000011000010110111001100100001000000100100100100000011010000110000101110110011001010010000001110111011010010111010001101000001000000110110101100101001000000110110101111001001000000110001101101100011000010111001101110011011011010110000101110100011001010111001100101100001000000101011001100001011100100110111101101111011011100010000001000010011000010111001101101000011110010110000101101011011000010111001001101100011000010010000001100001011011100110010000100000010100110110000101101101011101010110010101101100001000000100001001100101011100100111001101110100011011110110111000101110',
#     '001001110010011100'
# )
# print(res)

# STEP 5 
# Then DNA sequence D is complemented using Table 3 and named as K. 
def complement_DNA_sequence(key, XOR_Db_Pb_Res) -> str:
    D = key

    K = ''
    for letter in D:
        K += text_cryptography_helpers.dna_complement(letter)
    # print(f'K: {K}')

    # At the same time R is complemented using one’s complement operation and the resulting value is titled as R̄.
    res = ''
    for bit in list(XOR_Db_Pb_Res):
        res += text_cryptography_helpers.ones_complement(bit)
    # print(f'R̄: {res}')

    return res

# complement_DNA_sequence(text_cryptography_helpers.key, '010110110011000000110000001110100011000000110000001110100011000000110011001011100011100100110011001100000101110100100000001011010010000001010011011100000110010101100001011010110110010101110010001000000011000100100000010011110110101101100001011110010010111000100000010100000110010101110010011001100110010101100011011101000010111000100000010010000110100100100000011101000110100001100101011100100110010100101110001000000101011101100101011011000110001101101111011011010110010100100000011101000110111100100000011011110111010101110010001000000110100101101110011101000110010101110010011101100110100101100101011101110010000001110111011010010111010001101000001000000101001001100001011011100110101001101001011101100010000001000010011010000110000101101001011100100010111000100000010010010110110100100000010101000110000101101110011011010110000101111001011010010010000001001110011000010110111001100100011000010110111000100000011000010110111001100100001000000100100100100000011010000110000101110110011001010010000001110111011010010111010001101000001000000110110101100101001000000110110101111001001000000110001101101100011000010111001101110011011011010110000101110100011001010111001100101100001000000101011001100001011100100110111101101111011011100010000001000010011000010111001101101000011110010110000101101011011000010111001001101100011000010010000001100001011011100110010000100000010100110110000101101101011101010110010101101100001000000100001001100101011100100111001101110100011011111111001010110010')

# STEP 6 
# Then K is encrypted as per the rules explained in Sect. 4.2 and is termed as KE.
def encrypt_K(K) -> str:
    # Step 1: The total number of DNA nucleotides present in K is counted and then divided by 3. If the remainder is zero then K 
    # remains unchanged, otherwise “X” is added to the right side of K. The number of “X” added is equal to the difference between 3 
    # and the remainder.
    # K = 'ACTGACTAG'  # Example-1
    # K = 'ACTG'       # Example-2
    if len(K)%3 != 0:
        K += 'X'*(3 - len(K)%3)
    # print(K)

    # Step 2: Now, the DNA nucleotides of the chosen DNA sequence are to be grouped in such a manner that each group has exactly three 
    # nucleotides. The grouping starts from the leftmost side nucleotide. Then using Table 5 decimal values are assigned to each group.
    # K = 'ACTGACGTGCXX' # Example-3
    decimal_values = ''
    for i in range(0,len(K),3):
        group = K[i:i+3]
        decimal_values += str(text_cryptography_helpers.permutation_table[group])
        # print(decimal_values)
    # print(f'Decimal values: {decimal_values}')

    # Step 3: After getting the decimal values for the corresponding groups, they are concatenated sequentially from left to right to 
    # get an intermediate string.
    KE = ''
    for val in list(decimal_values):
        KE += text_cryptography_helpers.substitution_table[val]
    # print(f'KE: {KE}')

    return KE

# res = encrypt_K(text_cryptography_helpers.key)
# print(res)

# STEP 7  - return R and KE 