# Requirements:
# - this service will be a HOF that takes as arguments the encryption algorithm, the plaintext, & the X of processes to run
# - the service should have a performance analysis function which times the total encryption time
# - the service should have a logging function which writes the results to a CSV for further analysis
# 
# Steps:
# 1) splice the plaintext into X equal chunks (mod X) and store them in an array of length X
# 2) load X Process objects into an array with the target = encryption algorithm and the argument = the plaintext chunk
# 3) run X Processes concurrently, making sure to time them
# 4) write the resulting time to the CSV file, along with the arguments metadata

def multiprocessing_service(encryption_algorithm: function, plaintext: str, process_count: int) -> None:
    # Step 1: splice the plaintext into equal chunks (mod process_count) and store in an array
    # Step 2: load X Process objects into an array with the target = encryption algorithm and the argument = the plaintext chunk
    # Step 3: run X Processes concurrently, making sure to time them
    # Step 4: write the resulting time to the CSV file, along with the arguments metadata
    return 