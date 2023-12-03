'''
File: text_encryption_service.py
Description: The text encryption service
'''

import time
from threading import Thread


def text_encryption_service():
    time.sleep(5)
    print("completed text encryption")



t1 = Thread(target=text_encryption_service)
t2 = Thread(target=text_encryption_service)
t3 = Thread(target=text_encryption_service)

t1.start()
t2.start()
t3.start()