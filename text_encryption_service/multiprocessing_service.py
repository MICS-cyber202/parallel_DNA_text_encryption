# Requirements:
# - this service will be a HOF that takes as arguments the encryption algorithm, the plaintext, the key, & the X of processes to run
# - the service should have a performance analysis function which times the total encryption time
# - the service should have a logging function which writes the results to a CSV for further analysis
# 
# Steps:
# 1) splice the plaintext into X equal chunks (mod X) and store them in an array of length X
# 2) load X Process objects into an array with the target = encryption algorithm and the argument = the plaintext chunk
# 3) run X Processes concurrently, making sure to time them
# 4) write the resulting time to the CSV file, along with the arguments metadata

from multiprocessing import Process 
import os
import textwrap
from typing import Callable

def multiprocessing_service(encryption_algorithm: Callable[[str, str], str], plaintext: str, key: str, process_count: int) -> None:
    # Step 1: splice the plaintext into equal chunks (mod process_count) and store in an array
    # Step 2: load X Process objects into an array with the target = encryption algorithm and the argument = the plaintext chunk and the key
    # Step 3: run X Processes concurrently, making sure to time them
    # Step 4: write the resulting time to the CSV file, along with the arguments metadata
    return 

# helper functions

# chunk_plaintext takes the plaintext and chunk_count and returns an array of chunk_count # strings
# if len(plaintext) / chunk_count != 0 (i.e. there is a remainder), the final chunk is equal to residue
def chunk_plaintext(plaintext: str, chunk_count: int) -> str:
    chunk_len = len(plaintext) // chunk_count
    chunks = textwrap.wrap(plaintext, chunk_len)
    return chunks

# load_processes takes the encryption function, plaintext chunks, key, and process_count and returns an array of process_count # processes
def load_processes(encryption_algorithm: Callable[[str, str], str], plaintext_chunks: list, key: str, process_count: int) -> list:
    # handle the edge case where the # of chunks is not equal to the number of desired processes
    if len(plaintext_chunks) != process_count:
        raise Exception("The number of chunks must be equal to specified number of processes")
    
    encryption_processes = []
    for i in range(0, process_count):
        encryption_processes.append(Process(target=encryption_algorithm, args=(plaintext_chunks[i], key,)))
    return encryption_processes



# print(chunk_plaintext("aaaaaasaaaaaaaaaaaaaaaaaaaaa", 5))    

def dummy_method(arg1: str, arg2: str) -> str:
    return "dummy"

print(load_processes(dummy_method, ["aaa", "aaa", "aaa", "aaa", "aaa"], "abcde", 5))