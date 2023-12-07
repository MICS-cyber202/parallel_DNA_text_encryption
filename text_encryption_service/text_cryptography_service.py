'''
File: text_encryption_service.py
Description: The text encryption service
'''

# import sys
# import time
from threading import Thread
import text_cryptography_helpers
import text_encryption_functions
import file_processor

# get the transcript file loaded as a string
# sys.path.insert(1, '../file_processor')

# make sure this runs synchronously
def DNA_text_encryption(plaintext: str, key: str) -> tuple[str, str]:

    # STEP 2
    encoded_plaintext = text_encryption_functions.convert_plaintext_to_8bit(plaintext)
    
    # STEP 3
    DNA_encoded_key = text_encryption_functions.generate_DNA_sequence_from_key(key)
    
    # STEP 4
    XOR_Pb_Db_res = text_encryption_functions.XOR_Pb_Db(encoded_plaintext, DNA_encoded_key)
    
    # STEP 5 -- what is done with the result of this function????
    R = text_encryption_functions.complement_DNA_sequence(key, XOR_Pb_Db_res)

    # STEP 6
    KE = text_encryption_functions.encrypt_K(key)

    print('R: ', R)
    print('KE: ', KE)
    return [R, KE]


print(len(file_processor.plaintext_string))
part1_of_3 = file_processor.plaintext_string[:len(file_processor.plaintext_string) // 3]
part2_of_3 = file_processor.plaintext_string[len(file_processor.plaintext_string) // 3:(2 * len(file_processor.plaintext_string) // 3)]
part3_of_3 = file_processor.plaintext_string[(2 * len(file_processor.plaintext_string) // 3):]
# print(part1_of_3)
# print(part2_of_3)
# print(part3_of_3)
# 27854 / 5 = 5570 mod 4

# res = DNA_text_encryption(file_processor.plaintext_string, text_cryptography_helpers.key)   
# print("R: ", res[0])
# print("KE: ", res[1])

# to do: 
# - decryption

t1 = Thread(target=DNA_text_encryption, args=[part1_of_3, text_cryptography_helpers.key])
t2 = Thread(target=DNA_text_encryption, args=[part2_of_3, text_cryptography_helpers.key])
t3 = Thread(target=DNA_text_encryption, args=[part3_of_3, text_cryptography_helpers.key])

t1.start()
t2.start()
t3.start()