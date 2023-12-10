import itertools
import datetime
import random

def gen_sequence(strand_length):
    nucleotides = 'ACTG'
    seq = []
    
    for output in itertools.product(nucleotides, repeat = strand_length):
        seq.append(''.join(output))
    return(seq)

def generate_dna_encoding_table(num_characters, strand_length):
    seq = gen_sequence(strand_length)
    random.shuffle(seq)
    selected_seq = seq[0:num_characters]
    
    character_list = list(map(chr, range(32, 32 + num_characters)))

    keys = character_list
    values = selected_seq

    dna_encoding_dict = dict(zip(keys, values))
    return(dna_encoding_dict)

def generate_intron_sequence():
    return(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))

def generate_amino_acid_lookup_table():
    
    x = gen_sequence(strand_length = 2)
    y = gen_sequence(strand_length = 2)
    
    
    combo = []
    for e1, e2 in itertools.product(x, y):
        combo += [str(e1+str(e2))]
    random.shuffle(combo)

    ciphercodes = [
    'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'R1', 'R2', 'R3', 
    'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'RA', 'RB', 'RC', 'RD', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 
    'N7', 'N8', 'N9', 'NA', 'NB', 'NC', 'ND', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 
    'DA', 'DB', 'DC', 'DD', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC',
    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'EA', 'EB', 'EC', 'ED', 'Q1', 'Q2', 'Q3', 
    'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'QA', 'QB', 'QC', 'QD', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 
    'G7', 'G8', 'G9', 'GA', 'GB', 'GC', 'GD', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 
    'HA', 'HB', 'HC', 'HD', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'IA', 'IB', 'IC',
    'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'LA', 'LB', 'LC', 'LD', 'K1', 'K2', 'K3', 
    'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'KA', 'KB', 'KC', 'KD', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 
    'M7', 'M8', 'M9', 'MA', 'MB', 'MC', 'MD', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 
    'FA', 'FB', 'FC', 'FD', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'PA', 'PB', 'PC',
    'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'SA', 'SB', 'SC', 'SD', 'T1', 'T2', 'T3', 
    'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'TA', 'TB', 'TC', 'TD', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 
    'W7', 'W8', 'W9', 'WA', 'WB', 'WC', 'WD', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 
    'YA', 'YB', 'YC', 'YD', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'VA', 'VB', 'VC']
    random.shuffle(ciphercodes)
    
    aa_dict = dict(zip(combo, ciphercodes))
    return aa_dict

encoding_table_1 = generate_dna_encoding_table(num_characters = 96, strand_length = 4)
encoding_table_2 = generate_dna_encoding_table(num_characters = 96, strand_length = 4)
generated_intron_sequence = generate_intron_sequence()
aa_tbl = generate_amino_acid_lookup_table()

# Step 1 
def convert_to_dna(string, encoding_table):

    dna_encoding = []
    
    for c in string:
        dna_encoding.append(encoding_table[c])
    return(dna_encoding)

def convert_plaintext_to_dna(m):
    
    if(len(m) %2 != 0):
        m = m + ' '# add a space to make the string length even and thus splittable
    
    first_half  = m[:len(m)//2]
    second_half = m[len(m)//2:]
    
    dna_1 = convert_to_dna(first_half, encoding_table_1)
    dna_2 = convert_to_dna(second_half, encoding_table_2)
    
    return((dna_1, dna_2))


# Step 2
def convert_dna_to_binary(dna_strand):
    res = ''
    for strand in dna_strand:
        for segment in strand:
            converted = segment.replace('A', '00').replace('T', '01').replace('C', '10').replace('G', '11')
            res += converted
    return res

# Step 3
def adjust_key_length(intron_seq, seq):
    
    # When encrypting:
        # seq = dna_binary
    # When decrypting:
        # seq = xnor_result
    
    msg_len = len(seq)
    initial_key = '{0:0b}'.format(int(intron_seq))
    initial_key_len = len(initial_key)
    
    whole_repeats = int(msg_len / initial_key_len)
    fractional_repeats = msg_len % initial_key_len
    
    return initial_key * whole_repeats + initial_key[:fractional_repeats]

def xnor_operation(dna_binary, dna_strands):
    
    final_key = adjust_key_length(intron_seq = generated_intron_sequence, 
                                  seq = convert_dna_to_binary(dna_strands))
    
    xnor_result = ''
    for c in range(0, len(dna_binary)):
        if final_key[c] == dna_binary[c]:
            xnor_result += '1'
        else:
            xnor_result += '0'
    return xnor_result

# Step 4 (same as Decryption Step 2)
def convert_binary_to_dna(binary_string):
    
    dna_string = ''
    
    for n in range(0, int(len(binary_string)/2)):
        if binary_string[2 * n:2 * n+2] == '00':
            dna_string += 'A'
        if binary_string[2 * n:2 * n+2] == '01':
            dna_string += 'T'
        if binary_string[2 * n:2 * n+2] == '10':
            dna_string += 'C'
        if binary_string[2 * n:2 * n+2] == '11':
            dna_string += 'G'
        
    dna_string_len = len(dna_string)
    
    left_half = dna_string[:int(dna_string_len / 2)]
    right_half = dna_string[int(dna_string_len / 2):]
        
    left_result = [left_half[i:i+4] for i in range(0, len(left_half), 4)]
    right_result = [right_half[i:i+4] for i in range(0, len(right_half), 4)]
    
    return((left_result, right_result))

# Step 5
def convert_dna_to_mRNA(dna):
    
    combined_strand = ''
    
    for half in dna:
        combined_strand += ''.join(half)    
    
    mRNA = combined_strand.replace('T', 'U')
    
    return mRNA

# Step 6
def convert_mRNA_to_tRNA(mRNA):
    # A-U, U-A, G-C, C-G
    
    mapping = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    tRNA = "".join([mapping.get(c,c) for c in mRNA])
    
    return tRNA

# Step 7
def convert_tRNA_to_DNA(tRNA):
    dna = tRNA.replace('U', 'T')
    return dna

# Step 8 
def split_and_rotate(strg, operation):
    
    string_len = len(strg)
    
    left_half = strg[:int(string_len / 2)]
    right_half = strg[int(string_len / 2):]
    
    if operation == 'e':
        n = -1
        
    if operation == 'd':
        n = 1
    
    left_result = left_half[n:] + left_half[:n]
    right_result = right_half[n:] + right_half[:n]
    
    result = left_result + right_result
        
    return result

# Step 9
def convert_dna_to_ciphertext(dna, aa_lookup_table):
    
    ciphertext = ''
    
    dna = [dna[i:i+4] for i in range(0, len(dna), 4)]

    for entity in dna:
        ciphertext += aa_lookup_table[entity]
        
    return ciphertext

def encryption_process(m, num_round_functions):
    
# Step 1 - plaintext to dna
    dna_strands = convert_plaintext_to_dna(m)
    for j in range(0, num_round_functions):
        dna_binary = convert_dna_to_binary(dna_strand = dna_strands)
        xnor_result = xnor_operation(dna_binary, dna_strands)
        transformation_dna = convert_binary_to_dna(binary_string = xnor_result)
        mRNA_generated = convert_dna_to_mRNA(dna = transformation_dna)
        tRNA_generated = convert_mRNA_to_tRNA(mRNA = mRNA_generated)
        dna_generated = convert_tRNA_to_DNA(tRNA = tRNA_generated)
        split_rotate_result = split_and_rotate(strg = dna_generated, operation = 'e')
        # End-of-Cycle adjustments
        dna_strands = ((split_rotate_result[:len(split_rotate_result)//2], 
                        split_rotate_result[len(split_rotate_result)//2:]))
#         print('End of Round :', j)
#         print('Current Encrypted Text is :', split_rotate_result)
        
    ciphertext = convert_dna_to_ciphertext(dna = split_rotate_result, 
                                           aa_lookup_table = aa_tbl)
    return ciphertext

# Step 1
def convert_dna_to_plaintext(dna):
    
    plaintext_left_half = ''
    for strand in dna[0]:
        for key, value in encoding_table_1.items():
            if value == strand:
                plaintext_left_half += key
        
    plaintext_right_half = ''
    for strand in dna[1]:
         for key, value in encoding_table_2.items():
                if value == strand:
                    plaintext_right_half += key

    return([plaintext_left_half + plaintext_right_half])

# Step 2
def convert_binary_to_dna(binary_string):
    
    dna_string = ''
    
    for n in range(0, int(len(binary_string)/2)):
#         print(binary_string[2 * n:2 * n+2])
        if binary_string[2 * n:2 * n+2] == '00':
            dna_string += 'A'
        if binary_string[2 * n:2 * n+2] == '01':
            dna_string += 'T'
        if binary_string[2 * n:2 * n+2] == '10':
            dna_string += 'C'
        if binary_string[2 * n:2 * n+2] == '11':
            dna_string += 'G'
        
    dna_string_len = len(dna_string)
    
    left_half = dna_string[:int(dna_string_len / 2)]
    right_half = dna_string[int(dna_string_len / 2):]
        
    left_result = [left_half[i:i+4] for i in range(0, len(left_half), 4)]
    right_result = [right_half[i:i+4] for i in range(0, len(right_half), 4)]
    
    return((left_result, right_result))
    

# Step 3
def rev_xnor_operation(xnor_result):
    
    final_key = adjust_key_length(intron_seq = generated_intron_sequence, 
                                  seq = xnor_result)
    
    rev_xnor_result = ''
    for c in range(0, len(xnor_result)):
        if final_key[c] == xnor_result[c]:
            rev_xnor_result += '1'
        else:
            rev_xnor_result += '0'
    return rev_xnor_result

# Step 4 (same function as used in Encryption Step 2)

# Step 5
def convert_mRNA_to_dna(mRNA):
    dna = mRNA.replace('U', 'T')
    return dna

# Step 6
def convert_tRNA_to_mRNA(tRNA):
    # U-A, A-U, C-G, G-C
    mapping = {'U':'A', 'A':'U', 'G':'C', 'C':'G'}
    mRNA = "".join([mapping.get(c,c) for c in tRNA])
    return mRNA

# Step 7
def convert_dna_to_tRNA(dna):
    tRNA = dna.replace('T', 'U')
    return tRNA

# Step 8 (same function as used in Encryption step 8)

# Step 9
def convert_ciphertext_to_dna(ciphertext, aa_lookup_table):
    
    ciphertext = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    dna_result = ''
    rev_aa_lookup_table = dict(zip(list(aa_lookup_table.values()), 
                                   list(aa_lookup_table.keys())))
    
    for c in ciphertext:
        dna_result += rev_aa_lookup_table[c]
        
    return dna_result


def encryption_process(m, num_round_functions):
    
# Step 1 - plaintext to dna
    dna_strands = convert_plaintext_to_dna(m)
    for j in range(0, num_round_functions):
        dna_binary = convert_dna_to_binary(dna_strand = dna_strands)
        xnor_result = xnor_operation(dna_binary, dna_strands)
        transformation_dna = convert_binary_to_dna(binary_string = xnor_result)
        mRNA_generated = convert_dna_to_mRNA(dna = transformation_dna)
        tRNA_generated = convert_mRNA_to_tRNA(mRNA = mRNA_generated)
        dna_generated = convert_tRNA_to_DNA(tRNA = tRNA_generated)
        split_rotate_result = split_and_rotate(strg = dna_generated, operation = 'e')
        # End-of-Cycle adjustments
        dna_strands = ((split_rotate_result[:len(split_rotate_result)//2], 
                        split_rotate_result[len(split_rotate_result)//2:]))
#         print('End of Round :', j)
#         print('Current Encrypted Text is :', split_rotate_result)
        
    ciphertext = convert_dna_to_ciphertext(dna = split_rotate_result, 
                                           aa_lookup_table = aa_tbl)
    return ciphertext



# DECRYPTION


# Step 1
def convert_dna_to_plaintext(dna):
    
    plaintext_left_half = ''
    for strand in dna[0]:
        for key, value in encoding_table_1.items():
            if value == strand:
                plaintext_left_half += key
        
    plaintext_right_half = ''
    for strand in dna[1]:
         for key, value in encoding_table_2.items():
                if value == strand:
                    plaintext_right_half += key

    return([plaintext_left_half + plaintext_right_half])

# Step 2
def convert_binary_to_dna(binary_string):
    
    dna_string = ''
    
    for n in range(0, int(len(binary_string)/2)):
#         print(binary_string[2 * n:2 * n+2])
        if binary_string[2 * n:2 * n+2] == '00':
            dna_string += 'A'
        if binary_string[2 * n:2 * n+2] == '01':
            dna_string += 'T'
        if binary_string[2 * n:2 * n+2] == '10':
            dna_string += 'C'
        if binary_string[2 * n:2 * n+2] == '11':
            dna_string += 'G'
        
    dna_string_len = len(dna_string)
    
    left_half = dna_string[:int(dna_string_len / 2)]
    right_half = dna_string[int(dna_string_len / 2):]
        
    left_result = [left_half[i:i+4] for i in range(0, len(left_half), 4)]
    right_result = [right_half[i:i+4] for i in range(0, len(right_half), 4)]
    
    return((left_result, right_result))
    

# Step 3
def rev_xnor_operation(xnor_result):
    
    final_key = adjust_key_length(intron_seq = generated_intron_sequence, 
                                  seq = xnor_result)
    
    rev_xnor_result = ''
    for c in range(0, len(xnor_result)):
        if final_key[c] == xnor_result[c]:
            rev_xnor_result += '1'
        else:
            rev_xnor_result += '0'
    return rev_xnor_result

# Step 4 (same function as used in Encryption Step 2)

# Step 5
def convert_mRNA_to_dna(mRNA):
    dna = mRNA.replace('U', 'T')
    return dna

# Step 6
def convert_tRNA_to_mRNA(tRNA):
    # U-A, A-U, C-G, G-C
    mapping = {'U':'A', 'A':'U', 'G':'C', 'C':'G'}
    mRNA = "".join([mapping.get(c,c) for c in tRNA])
    return mRNA

# Step 7
def convert_dna_to_tRNA(dna):
    tRNA = dna.replace('T', 'U')
    return tRNA

# Step 8 (same function as used in Encryption step 8)

# Step 9
def convert_ciphertext_to_dna(ciphertext, aa_lookup_table):
    
    ciphertext = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    dna_result = ''
    rev_aa_lookup_table = dict(zip(list(aa_lookup_table.values()), 
                                   list(aa_lookup_table.keys())))
    
    for c in ciphertext:
        dna_result += rev_aa_lookup_table[c]
        
    return dna_result

def decryption_process(ciphertext, num_round_functions):
    dna_from_ciphertext = convert_ciphertext_to_dna(ciphertext = ciphertext, 
                                                    aa_lookup_table = aa_tbl)    
    for j in range(0, num_round_functions):
        dna_generated = split_and_rotate(strg = dna_from_ciphertext, operation = 'd') # encryption_result
        tRNA_generated = convert_dna_to_tRNA(dna = dna_generated)  # dna_generated
        mRNA_generated = convert_tRNA_to_mRNA(tRNA = tRNA_generated) 
        transformation_dna = convert_mRNA_to_dna(mRNA = mRNA_generated) 
        xnor_result = convert_dna_to_binary(dna_strand = transformation_dna) 
        rev_xnor_result = rev_xnor_operation(xnor_result)
        dna_strands = convert_binary_to_dna(binary_string = rev_xnor_result)
        combined_strand = ''
        for half in dna_strands:
            combined_strand += ''.join(half)    
        dna_from_ciphertext = combined_strand
#         print('End of Round :', j)
#         print('Current Decrypted Text is :', dna_from_ciphertext)
    m = convert_dna_to_plaintext(dna = dna_strands)
    return(m)


plaintext_msg = "a" * 100

# Encryption
generated_ciphertext = encryption_process(m = plaintext_msg, num_round_functions = 10)
print('ciphertext :', generated_ciphertext)

# Decryption
decryption_process(ciphertext = generated_ciphertext, num_round_functions = 10)


