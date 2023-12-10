import text_cryptography_helpers


# STEP 6

# Get decimal values from substitution table 
def get_decimal_values(KE) -> str:
    decimal_values = ''
    for i in range(0,len(KE),4):
        # print(KE[i:i+4])
        decimal_values += str(list(text_cryptography_helpers.substitution_table.keys())[list(text_cryptography_helpers.substitution_table.values()).index(KE[i:i+4])])
    # print(f'Decimal values: {decimal_values}')

    K = ''
    for i in range(0,len(decimal_values),2):
        K += str(list(text_cryptography_helpers.permutation_table.keys())[list(text_cryptography_helpers.permutation_table.values()).index(int(decimal_values[i:i+2]))])


    # K = 'ACTGACGTGCXX'
    K = K.replace('X','')
    return K

# STEP 5
def step5(K) -> tuple[str, str]:
    D = ''
    for letter in K:
        D += text_cryptography_helpers.dna_complement(letter)
    # print(f'D: {D}')

    R = ''
    for bit in list(R̄):
        R += text_cryptography_helpers.ones_complement(bit)
    
    return [R, D]

# STEP 6
def step6(D):
    Db = ''
    for letter in D:
        Db+= text_cryptography_helpers.dna_dict[letter]
    return Db
    # print(f'Db: {Db}')

# STEP 7
def step7(R, Db) -> str:
    if len(R)<len(Db):
        R = '0'*(len(Db)-len(R))+R
    elif len(R)>len(Db):
        Db = '0'*(len(R)-len(Db))+Db

    Pb = ''
    for i in range(0,len(Db)):
        Pb += text_cryptography_helpers.xor(R[i],Db[i])
    
    return Pb

# Step 8
def step8(Pb) -> str:
    ascii_values = []
    while len(Pb)>8:
        ascii_values.append(int(Pb[:8],2))
        Pb = Pb[8:]
    ascii_values.append(int(Pb,2))
    # print(ascii_values)

    plaintext = ''
    for i in ascii_values:
        plaintext += chr(i)

    return plaintext    


def source_E_decryption(ciphertext, modified_key, KE):
    # STEP 6 
    # Get decimal values from substitution table 
    decimal_values = ''
    for i in range(0,len(KE),4):
        # print(KE[i:i+4])
        decimal_values += str(list(text_cryptography_helpers.substitution_table.keys())[list(text_cryptography_helpers.substitution_table.values()).index(KE[i:i+4])])
    # print(f'Decimal values: {decimal_values}')
    
    K = ''
    for i in range(0,len(decimal_values),2):
        K += str(list(text_cryptography_helpers.permutation_table.keys())[list(text_cryptography_helpers.permutation_table.values()).index(int(decimal_values[i:i+2]))])
    
    
    # K = 'ACTGACGTGCXX'
    K = K.replace('X','')
    # print(f'K: {K}')
    
    # STEP 5
    D = ''
    for letter in K:
        D += text_cryptography_helpers.dna_complement(letter)
    # print(f'D: {D}')
    
    R = ''
    for bit in list(R̄):
        R += text_cryptography_helpers.ones_complement(bit)
    # print(f'R: {R}')
    
    # STEP 3
    Db = ''
    for letter in D:
        Db+= text_cryptography_helpers.dna_dict[letter]
    # print(f'Db: {Db}')
    
    # STEP 4
    if len(R)<len(Db):
        R = '0'*(len(Db)-len(R))+R
    elif len(R)>len(Db):
        Db = '0'*(len(R)-len(Db))+Db
    
    Pb = ''
    for i in range(0,len(Db)):
        Pb += text_cryptography_helpers.xor(R[i],Db[i])
    # print(f' Pb: {Pb}')
    
    # STEP 2
    # Removing the '0' padding
    # Pb = Pb[Pb.find('1'):]
    
    ascii_values = []
    while len(Pb)>8:
        ascii_values.append(int(Pb[:8],2))
        Pb = Pb[8:]
    ascii_values.append(int(Pb,2))
    # print(ascii_values)
    
    plaintext = ''
    for i in ascii_values:
        plaintext += chr(i)
    return (plaintext)
