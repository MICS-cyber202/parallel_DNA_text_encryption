import os
from dotenv import load_dotenv

load_dotenv()

plaintext_file_path = os.getenv('PLAINTEXT_PATH')
plaintext_file = open(plaintext_file_path)
plaintext_string = plaintext_file.read()
