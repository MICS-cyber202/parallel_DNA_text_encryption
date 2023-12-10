# Requirements:
# - this service will be a HOF that takes as arguments the encryption algorithm, the plaintext, the key, & the X of processes to run
# - the service should have a performance analysis function which times the total encryption time
# - the service should have a logging function which writes the results to a CSV for further analysis
# - the metrics should include: algorith_name, time_to_encrypt, process_count, 
#
# 
# Steps:
# 1) splice the plaintext into X equal chunks (mod X) and store them in an array of length X
# 2) load X Process objects into an array with the target = encryption algorithm and the argument = the plaintext chunk
# 3) run X Processes concurrently, making sure to time them
# 4) write the performance metrics to the CSV file, along with the arguments metadata

import csv
from multiprocessing import Process , freeze_support
import os
import textwrap
from time import perf_counter_ns, sleep
from typing import Callable

import varoon_implB
import text_cryptography_service
import text_cryptography_helpers
import file_processor

def multiprocessing_service(encryption_algorithm: Callable[[str, str], str], plaintext: str, key: str, process_count: int) -> None:
   
    plaintext = plaintext
    # Step 1: splice the plaintext into equal chunks (mod process_count) and store in an array
    plaintext_chunks = chunk_plaintext(plaintext, process_count)
    plaintext_chunks = plaintext_chunks[:process_count]
    print("plaintext chunks: ", plaintext_chunks)
    # Step 2: load X Process objects into an array with the target = encryption algorithm and the argument = the plaintext chunk and the key
    encryption_processes = load_processes(encryption_algorithm, plaintext_chunks, key, process_count)
    # Step 3: start the performance timer
    start_time = perf_counter_ns()
    # Step 4: run X Processes concurrently
    run_processes(encryption_processes)
    # Step 5: stop the performance timer
    end_time = perf_counter_ns()
    # Step 6: write the performance metrics to the CSV file, along with the arguments metadata
    time_to_run=end_time-start_time
    performance_metric_csvrow=["text_encryption_algorithm", process_count, len(plaintext), time_to_run]
    csv_file_path = "/Users/samuelberston/Documents/MICS/courses/CYBER202/Project/Parallel_Text_Encrpytion/performance_metrics.csv"
    print("csvrow: ", performance_metric_csvrow)
    write_metrics_to_csv(performance_metric_csvrow, csv_file_path)

# helper functions

# FIX THIS TO HANDLE MODULAR RESIDUE!!!!
# chunk_plaintext takes the plaintext and chunk_count and returns an array of chunk_count # strings
# if len(plaintext) / chunk_count != 0 (i.e. there is a remainder), the final chunk is equal to residue
def chunk_plaintext(plaintext: str, chunk_count: int) -> str:
    chunk_len = len(plaintext) // chunk_count
    print("len", chunk_len)
    # mod = len(plaintext) % chunk_len
    # plaintext=plaintext[:len(plaintext) - mod]
    # print(plaintext)
    chunks = textwrap.wrap(plaintext, chunk_len)
    return chunks[:chunk_count]

# load_processes takes the encryption function, plaintext chunks, key, and process_count and returns an array of process_count # processes
def load_processes(encryption_algorithm: Callable[[str, str], str], plaintext_chunks: list, key: str, process_count: int) -> list:
    # handle the edge case where the # of chunks is not equal to the number of desired processes
    if len(plaintext_chunks) != process_count:
        raise Exception("The number of chunks must be equal to specified number of processes")
    
    encryption_processes = []
    for i in range(0, process_count):
        encryption_processes.append(Process(target=encryption_algorithm, args=(plaintext_chunks[i], key,)))
    return encryption_processes

# run_processes takes the loaded encryption_processes and runs them all concurrently
# to do - figure out the best place to collect performance metrics and write them to the CSV
# the function does not return anything 
def run_processes(encryption_processes: list[Process]) -> None:
    for i in range(0, len(encryption_processes)):
        runnable = encryption_processes[i]
        print(runnable)
        runnable.start()
    return

# write_metrics_to_csv takes a list of the metrics as csv and appends them to a csv file
def write_metrics_to_csv(metricsrow: list, csv_file_path: str) -> None:
    with open(csv_file_path, 'a', newline="\n") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(metricsrow) 
    return    

# check chunk_plaintext method works
# print(chunk_plaintext("aaaaaasaaaaaaaaaaaaaaaaaaaaa", 5))    


dummy_plaintext = "dummyplaintextdummyplaintextdummyplaintext"
dummy_key = "dummykey"

def dummy_method(arg1: str, arg2: str) -> str:
    sleep(3)
    print("dummy")
    return "dummy"

# check load_process method works
# print(load_processes(dummy_method, ["aaa", "aaa", "aaa", "aaa", "aaa"], "abcde", 5))

dummy_process1 = Process(target=dummy_method, args=("foo","bar",))
dummy_process2 = Process(target=dummy_method, args=("foo","bar",))
dummy_process3 = Process(target=dummy_method, args=("foo","bar",))
dummy_process4 = Process(target=dummy_method, args=("foo","bar",))
dummy_process5 = Process(target=dummy_method, args=("foo","bar",))

dummy_processes = [dummy_process1, dummy_process2, dummy_process3, dummy_process4, dummy_process5]

# print(dummy_processes)

if __name__ == '__main__':
    freeze_support() # only needed if running on Windows
    # check run_processes method works
    # print(run_processes(dummy_processes))
    for i in range(0, 10):
        print(os.cpu_count())
        multiprocessing_service(text_cryptography_service.DNA_text_encryption, file_processor.plaintext_string ,text_cryptography_helpers.key, 8)
    # print(chunk_plaintext(file_processor.plaintext_string, 2))